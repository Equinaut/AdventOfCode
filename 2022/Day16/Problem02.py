import copy

START_POSITION = "AA"
# Valve is (Name, Flow Rate, Distances = [(Name, Distance)])
valves = dict()

with open("input.txt") as file:
    for line in file.readlines():
        excludedValue = line[6:8]
        rate = int(line.split(";")[0].split("=")[1])
        if "valves" in line:
            connections = [(name, 1) for name in line.split("to valves ")[1][:-1].split(", ")]
        else:
            connections = [(name, 1) for name in line.split("to valve ")[1][:-1].split(", ")]
        
        valves[excludedValue] = (excludedValue, rate, connections)
valveCount = len(valves)

newValves = copy.deepcopy(valves)
for startVertex in list(valves.keys()):
    distances = {v: float("inf") for v in valves}
    queue = []
    for v in valves:
        queue.append(v)

    distances[startVertex] = 0
    while len(queue):
        u = min(queue, key = distances.get)
        queue.remove(u)
        uDistance = distances.get(u)
        for v,_ in valves[u][2]:
            vDistance = distances.get(v)
            alt = uDistance + 1
            if alt < vDistance:
                distances[v] = alt

    newValves[startVertex] = (valves[startVertex][0], valves[startVertex][1], list(distances.items()))

newValves = {name : value for name, value in newValves.items() if (value[1] > 0) or name == START_POSITION}

for excludedValue in newValves:
    distances = {name: (name, distance) for (name, distance) in newValves[excludedValue][2] if (distance > 0 and name in newValves) or (name == START_POSITION and excludedValue != START_POSITION)}
    newValves[excludedValue] = (newValves[excludedValue][0], newValves[excludedValue][1], distances)



# ------------------------------------------------------------------------------------------------------------------- #

def calculateDistance(order1):
    if order1 == []: return 0, 0, 0
    distance = valves[START_POSITION][2][order1[0]][1] + 1
    flowRate = valves[order1[0]][1]
    totalFlowRate = 0
    i = 0
    while i < len(order1) - 1:
        currentNode = order1[i]
        i += 1
        newDistance = valves[currentNode][2][order1[i]][1] + 1
        distance += newDistance
        totalFlowRate += flowRate * newDistance

        flowRate += valves[order1[i]][1]
    return distance, totalFlowRate

getPositionsCache = dict()
def getPositions(order1):
    if str(order1) in getPositionsCache: return getPositionsCache[str(order1)]
    distance1 = valves[START_POSITION][2][order1[0]][1] + 1
    distances1 = [distance1]
    flowRateIncreases1 = [valves[order1[0]][1]]
    flowRate1 = valves[order1[0]][1]

    i = 0
    while i < len(order1) - 1:
        currentNode = order1[i]
        i += 1
        newDistance1 = valves[currentNode][2][order1[i]][1] + 1
        distance1 += newDistance1
        flowRate1 += valves[order1[i]][1]
        distances1.append(distance1)
        flowRateIncreases1.append(valves[order1[i]][1])

    getPositionsCache[str(order1)] = distances1, distance1, flowRateIncreases1
    return getPositionsCache[str(order1)]

def calculateDistance2(order1, order2):
    totalFlowRate = 0
    distances1, distance1, flowRateIncreases1 = getPositions(order1)
    distances2, distance2, flowRateIncreases2 = getPositions(order2)
    for i in range(0, 27):
        flowRate = 0
        j = 0
        while j < len(distances1) and i > distances1[j]:
            flowRate += flowRateIncreases1[j]
            j += 1
        j = 0
        while j < len(distances2) and i > distances2[j]:
            flowRate += flowRateIncreases2[j]
            j += 1
        
        totalFlowRate += flowRate

    return distance1, distance2, totalFlowRate, flowRate
valves = copy.deepcopy(newValves)


states = [[]] # [Valves in order of opening]
energyReleased = dict() # State -> Energy released

while len(states):
    currentState = states.pop(0)
    distance = 0
    if len(currentState) > 0:
        distance, flowRate = calculateDistance(currentState)
        if distance > 26: 
            continue
        energyReleased[",".join(currentState)] = flowRate


    for excludedValue in valves:
        if excludedValue in currentState: continue
        if excludedValue == START_POSITION: continue
        states.append(currentState + [excludedValue])

energyReleasedSorted = []
energyReleasedSortedPartitioned = dict()
for valve in valves:
    energyReleasedSortedPartitioned[valve] = []

for key, value in energyReleased.items():
    newValue = (key.split(","), value, set(key.split(",")))
    energyReleasedSorted.append(newValue)
    for valve in valves:
        if valve not in newValue[2]:
            energyReleasedSortedPartitioned[valve].append(newValue)

energyReleasedSorted.sort(key = lambda a: a[1], reverse=True)
for valve in valves:
    energyReleasedSortedPartitioned[valve].sort(key = lambda a: a[1], reverse = True)

maxValves = 0
for i, (human, humanValue, humanSet) in enumerate(energyReleasedSorted):
    breakValue = 0
    for j, (elephant, elephantValue, elephantSet) in enumerate(energyReleasedSortedPartitioned[human[0]]):
        if elephantSet.isdisjoint(humanSet):
            d1, d2, a, b = calculateDistance2(human, elephant)
            if max(d1, d2) > 26: continue

            if a > maxValves:
                maxValves = a
            breakValue = elephantValue

        if elephantValue > breakValue: break
print(f"The answer is {maxValves}")