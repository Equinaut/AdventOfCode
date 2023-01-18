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
    
    if GeodeCount + GeodeRobotCount * (MAX_TIME - Time) + ((MAX_TIME - Time) * (MAX_TIME - Time + 1) / 2 + 1) < maxGeodes:
        return []

    doneOre = doneClay = doneObsidian = doneGeode = False

    needsOreBot = OreRobotCount < max(map(lambda cost: cost[0], costs))
    needsClayBot = ClayRobotCount < max(map(lambda cost: cost[1], costs))
    needsObsidianBot = ObsidianRobotCount < max(map(lambda cost: cost[2], costs))

    for i in range(0, MAX_TIME - Time):
        if needsOreBot and (not doneOre) and canAfford(newStateNoBuild(i, state), OreRobotCost):
            nextStates.append(
                (
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - OreRobotCost[0], OreRobotCount + 1),
                    (ClayCount + (i + 1) * ClayRobotCount - OreRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - OreRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - OreRobotCost[3], GeodeRobotCount)
                )
            )
            doneOre = True
            
        if needsClayBot and (not doneClay) and canAfford(newStateNoBuild(i, state), ClayRobotCost):
            nextStates.append(
                (
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - ClayRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - ClayRobotCost[1], ClayRobotCount + 1),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - ClayRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - ClayRobotCost[3], GeodeRobotCount)
                )
            )
            doneClay = True

        if needsObsidianBot and (not doneObsidian) and canAfford(newStateNoBuild(i, state), ObsidianRobotCost):
            nextStates.append(
                (
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - ObsidianRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - ObsidianRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - ObsidianRobotCost[2], ObsidianRobotCount + 1),
                    (GeodeCount + (i + 1) * GeodeRobotCount - ObsidianRobotCost[3], GeodeRobotCount)
                )
            )
            doneObsidian = True

        if (not doneGeode) and canAfford(newStateNoBuild(i, state), GeodeRobotCost):
            nextStates.append(
                (
                    Time + i + 1,
                    (OreCount + (i + 1) * OreRobotCount - GeodeRobotCost[0], OreRobotCount),
                    (ClayCount + (i + 1) * ClayRobotCount - GeodeRobotCost[1], ClayRobotCount),
                    (ObsidianCount + (i + 1) * ObsidianRobotCount - GeodeRobotCost[2], ObsidianRobotCount),
                    (GeodeCount + (i + 1) * GeodeRobotCount - GeodeRobotCost[3], GeodeRobotCount + 1)
                )
            )
            doneGeode = True
    return nextStates

def main(costs):
    states = [(1, (0, 1), (0, 0), (0, 0), (0, 0))]
    maxGeodes = 0
    while states:
        state = states.pop(0)
        geodes, geodeRobots = state[4]
        if (newMax := geodes + geodeRobots * (MAX_TIME - state[0] + 1)) > maxGeodes: maxGeodes = newMax
        states.extend(newStates(state, maxGeodes, costs))
    return maxGeodes

MAX_TIME = 24

blueprints = []


with open("input.txt") as file:
    for line in file.readlines():
        line = line.split(": ")[1].split(".")
        blueprints.append([])
        for robot in line[:-1]:
            costs = [0, 0, 0, 0]
            parts = robot.split("costs")[1][1:].split(" and ")
            for part in parts: costs[{"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}[part.split(" ")[1]]] = int(part.split(" ")[0])
            blueprints[-1].append(tuple(costs))

answer = 0
for i, costs in enumerate(blueprints):
    currentAnswer = main(costs)
    answer += (i + 1) * currentAnswer

print(f"The answer is {answer}")