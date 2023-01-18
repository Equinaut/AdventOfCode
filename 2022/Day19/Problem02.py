# A state is represented by 
# (
#   Time,
#   (OreCount, OreRobotCount),
#   (ClayCount, ClayRobotCount),
#   (ObsidianCount, ObsidianRobotCount),
#   (GeodeCount, GeodeRobotCount)
# )

def newStateNoBuild(timeDifference, state):
    (
        Time,
        (OreCount, OreRobotCount),
        (ClayCount, ClayRobotCount),
        (ObsidianCount, ObsidianRobotCount),
        (GeodeCount, GeodeRobotCount)
    ) = state

    return (
        Time + timeDifference,
        (OreCount + OreRobotCount * timeDifference, OreRobotCount),
        (ClayCount + ClayRobotCount * timeDifference, ClayRobotCount),
        (ObsidianCount + ObsidianRobotCount * timeDifference, ObsidianRobotCount),
        (GeodeCount + GeodeRobotCount * timeDifference, GeodeRobotCount)
    )

def canAfford(state, cost):
    (
        Time,
        (OreCount, OreRobotCount),
        (ClayCount, ClayRobotCount),
        (ObsidianCount, ObsidianRobotCount),
        (GeodeCount, GeodeRobotCount)
    ) = state

    return OreCount >= cost[0] and ClayCount >= cost[1] and ObsidianCount >= cost[2] and GeodeCount >= cost[3]

def newStates(state, maxGeodes, costs):
    nextStates = []
    (
        Time,
        (OreCount, OreRobotCount),
        (ClayCount, ClayRobotCount),
        (ObsidianCount, ObsidianRobotCount),
        (GeodeCount, GeodeRobotCount)
    ) = state

    OreRobotCost, ClayRobotCost, ObsidianRobotCost, GeodeRobotCost = costs
    
    if GeodeCount + GeodeRobotCount * (MAX_TIME - Time + 1) + ((MAX_TIME - Time) * (MAX_TIME - Time + 1) / 2 + 1) < maxGeodes: return []

    doneOre = doneClay = doneObsidian = doneGeode = False

    needsOreBot = OreRobotCount < max(map(lambda cost: cost[0], costs))
    needsClayBot = ClayRobotCount < max(map(lambda cost: cost[1], costs))
    needsObsidianBot = ObsidianRobotCount < max(map(lambda cost: cost[2], costs))

    for i in range(0, MAX_TIME - Time):
        if (not doneGeode) and canAfford(newStateNoBuild(i, state), GeodeRobotCost):
            nextStates.append((
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - GeodeRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - GeodeRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - GeodeRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - GeodeRobotCost[3], GeodeRobotCount + 1)
            ))
            doneGeode = True

        if needsObsidianBot and (not doneObsidian) and canAfford(newStateNoBuild(i, state), ObsidianRobotCost):
            nextStates.append((
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - ObsidianRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - ObsidianRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - ObsidianRobotCost[2], ObsidianRobotCount + 1),
                    (GeodeCount + (i + 1) * GeodeRobotCount - ObsidianRobotCost[3], GeodeRobotCount)
            ))
            doneObsidian = True

        if needsClayBot and (not doneClay) and canAfford(newStateNoBuild(i, state), ClayRobotCost):
            nextStates.append((
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - ClayRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - ClayRobotCost[1], ClayRobotCount + 1),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - ClayRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - ClayRobotCost[3], GeodeRobotCount)
                ))
            doneClay = True

        if needsOreBot and (not doneOre) and canAfford(newStateNoBuild(i, state), OreRobotCost):
            nextStates.append((
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - OreRobotCost[0], OreRobotCount + 1),
                    (ClayCount + (i + 1) * ClayRobotCount - OreRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - OreRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - OreRobotCost[3], GeodeRobotCount)
                ))
            doneOre = True
    return nextStates

sortingProperty = lambda state: state[4][1]

def getItem(states, maxSection):
    for i in range(maxSection, -1, -1):
        if i not in states or states[i] == []: continue
        return states[i].pop(0)
    return None


def main(costs):
    maxSection = 0
    states = {0: []}
    states[0].append((1, (0, 1), (0, 0), (0, 0), (0, 0)))

    doneStates = set()
    maxGeodes = 0
    j = 0
    while True:
        newItem = getItem(states, maxSection)
        if newItem is None: break
        state = newItem
        
        doneStates.add(state)

        j -= 1
        geodes, geodeRobots = state[4]
        if (newMax := geodes + geodeRobots * (MAX_TIME - state[0] + 1)) > maxGeodes:
            maxGeodes = newMax

        for newState in newStates(state, maxGeodes, costs):
            if newState[0] in doneStates: continue
            section = sortingProperty(newState)
            if section > maxSection: maxSection = section

            if section not in states:
                states[section] = [newState]
            else:
                current = states[section]
                current.append(newState)
            j += 1
            
    return maxGeodes

blueprints = []


with open("input.txt") as file:
    for line in file.readlines():
        line = line.split(": ")[1].split(".")
        blueprints.append([])
        for robot in line[:-1]:
            costs = [0,0,0,0]
            parts = robot.split("costs")[1][1:].split(" and ")
            for part in parts:
                if part.split(" ")[1] == "ore": costs[0] = int(part.split(" ")[0])
                if part.split(" ")[1] == "clay": costs[1] = int(part.split(" ")[0])
                if part.split(" ")[1] == "obsidian": costs[2] = int(part.split(" ")[0])
                if part.split(" ")[1] == "geode": costs[3] = int(part.split(" ")[0])
            blueprints[-1].append(tuple(costs))

MAX_TIME = 32
answer = 1

for i, costs in enumerate(blueprints[:3]):
    currentAnswer = main(costs)
    answer *= currentAnswer

print(f"The answer is {answer}")