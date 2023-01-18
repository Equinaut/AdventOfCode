import copy

START_POSITION = "AA"
# Valve is (Name, Flow Rate, Distances = [(Name, Distance)])
valves = dict()

with open("input.txt") as file:
    for line in file.readlines():
        valve = line[6:8]
        rate = int(line.split(";")[0].split("=")[1])
        connections = [(name, 1) for name in line.split("to valves " if "valves" in line else "to valve ")[1][:-1].split(", ")]
        
        valves[valve] = (valve, rate, connections)

def calculateDistance(order):
    if order == []: return 0, 0, 0
    distance = valves[START_POSITION][2][order[0]][1] + 1
    flowRate = valves[order[0]][1]
    totalFlowRate = 0
    i = 0
    while i < len(order) - 1:
        currentNode = order[i]
        i += 1
        newDistance = valves[currentNode][2][order[i]][1] + 1
        distance += newDistance
        totalFlowRate += flowRate * newDistance
        flowRate += valves[order[i]][1]
        
    return distance, totalFlowRate, totalFlowRate + (30 - distance) * flowRate

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
for valve in newValves:
    distances = {name: (name, distance) for (name, distance) in newValves[valve][2] if (distance > 0 and name in newValves) or (name == START_POSITION and valve != START_POSITION)}
    newValves[valve] = (newValves[valve][0], newValves[valve][1], distances)

valves = copy.deepcopy(newValves)
maxFlowRate = sum(value[1] for value in valves.values())
states = [[]]

maxD = 0
while len(states):
    order = states.pop(0)
    d, u, a = calculateDistance(order)
    if d >= 30: continue
    if u + (30 - d) * maxFlowRate < maxD: continue
    if a > maxD: maxD = a

    for nextValve in valves:
        if nextValve == START_POSITION: continue
        if nextValve in order: continue
        states.append(order + [nextValve])

print(f"The answer is {maxD}")