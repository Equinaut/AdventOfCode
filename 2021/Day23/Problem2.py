import copy
import time

startTime = time.perf_counter()

startState = {
    "hall": set(),
    "buckets": [
        ["A", "D", "D", "D"],
        ["C", "C", "B", "D"],
        ["B", "B", "A", "A"],
        ["B", "A", "C", "C"]
    ]
}

def allPossibleStates(energy, state):
    states = []

    for type, x in state["hall"]: #Hall to bucket
        homeBucket = {"A": 0, "B": 1, "C": 2, "D": 3}[type]
        if len(state["buckets"][homeBucket]) >= 4: continue
        if not all([i == type for i in state["buckets"][homeBucket]]): 
            continue

        minX, maxX = 0, 12
        for _, x2 in state["hall"]:
            if x2 > minX and x2 < x: minX = x2
            if x2 < maxX and x2 > x: maxX = x2
        homeBucketX = 3 + homeBucket * 2

        if homeBucketX > minX and homeBucketX < maxX:
            newState = copy.deepcopy(state)
            newState["hall"].remove((type, x))
            newState["buckets"][homeBucket].insert(0, type)

            newEnergy = 0
            newEnergy += abs(x - [3, 5, 7, 9][homeBucket])
            newEnergy += 5-len(newState["buckets"][homeBucket])
            newEnergy *= {"A": 1, "B": 10, "C": 100, "D": 1000}[type]
            newEnergy += energy

            states.append((newEnergy, newState))
    
    for i, bucket in enumerate(state["buckets"]): #Bucket to hall
        if len(bucket) == 0: continue
        correctType = "ABCD"[i]
        if all([j == correctType for j in bucket]): continue
        x = i*2 + 3

        minX, maxX = 0, 12
        for type2, x2 in state["hall"]:
            if x2 > minX and x2 < x: minX = x2
            if x2 < maxX and x2 > x: maxX = x2

        for x2 in range(minX + 1, maxX):
            if x2 in {3, 5, 7, 9}: continue
            newState = copy.deepcopy(state)
            item = newState["buckets"][i].pop(0)
            newState["hall"].add((item, x2))

            newEnergy = 0
            newEnergy += abs(x2 - x)
            newEnergy += 5 - len(bucket)

            newEnergy *= {"A": 1, "B": 10, "C": 100, "D": 1000}[item]
            newEnergy += energy
            states.append((newEnergy, newState))
    return states

def hashState(state):
    hall = ["." for i in range(0, 11)]
    for type, x in state["hall"]:
        hall[x-1] = type
    buckets = ["" for i in range(0, 4)]
    for i, bucket in enumerate(state["buckets"]):
        buckets[i] = "".join(bucket)
        buckets[i] = "."*(4 - len(buckets[i])) + buckets[i]
    return "".join(hall)+"".join(buckets)

def finished(state):
    if len(state["hall"]) > 0: return False

    for i, bucket in enumerate(state["buckets"]):
        if len(bucket) != 4: return False
        correctItem = "ABCD"[i]
        if any([item != correctItem for item in bucket]): return False
    return True

queue = []
def addToQueue(newEnergyWithH, newEnergy, steps, state):
    if len(queue) == 0 or newEnergyWithH > queue[-1][0]:
        queue.append((newEnergyWithH, newEnergy, steps, state))
        return
    if newEnergyWithH < queue[0][0]: 
        queue.insert(0, (newEnergyWithH, newEnergy, steps, state))
        return

    i = 0

    while newEnergyWithH > queue[i][0] and i < len(queue): i+=1
    queue.insert(i, (newEnergyWithH, newEnergy, steps, state))

def outputState(state):
    width = 13
    height = 7

    outputLines = [[" " for x in range(0, width)] for y in range(0, height)]
    for x in range(1, 12): outputLines[1][x] = "."
    for item, x in state["hall"]:
        outputLines[1][x] = item
    
    for x in [3,5,7,9]:
        for y in range(2, 6):
            outputLines[y][x] = "."
    for bucket, x in zip(state["buckets"], [3,5,7,9]):
        for i, item in enumerate(bucket[::-1]):
            outputLines[5-i][x] = item

    return ["".join(i) for i in outputLines]

def heuristic(state):
    value = 0
    # for i, bucket in enumerate(state["buckets"]):
    #     homeItem = "ABCD"[i]
    #     for item in bucket[1:]:
    #         if item != homeItem and item=="Z":
    #             value += {"A": 1, "B": 10, "C": 100, "D": 1000}[item] * 5
    # return value

    value = 0
    for item, x in state["hall"]:
        homeX = {"A": 3, "B": 5, "C": 7, "D": 9}[item]
        value+=(1 + abs(homeX - x)) * {"A": 1, "B": 10, "C": 100, "D": 1000}[item]

    for i, bucket in enumerate(state["buckets"]):
        bucketX = [3, 5, 7, 9][i]
        for k,j in enumerate(bucket):
            homeX = {"A": 3, "B": 5, "C": 7, "D": 9}[j]
            if bucketX != homeX:
                value+=(abs(homeX - bucketX)) * {"A": 1, "B": 10, "C": 100, "D": 1000}[j]
                value+=(5-(len(bucket)-k)) * {"A": 1, "B": 10, "C": 100, "D": 1000}[j]
    return value

def printState(state):
    print("\n".join(outputState(state)))
    print()

addToQueue(heuristic(startState), 0, 0, startState)
previouslyDone = set()

lastLogged = 0


while len(queue) > 0:
    energyWithH, energy, steps, state = queue.pop(0)
    
    if hashState(state) in previouslyDone: continue
    previouslyDone.add(hashState(state))
    
    newStates = allPossibleStates(energy, state)
    for newEnergy, newState in newStates:
        newEnergyWithH = newEnergy
        addToQueue(newEnergyWithH, newEnergy, steps + 1, newState)

        if finished(newState):
            print(f"The answer is {newEnergy}, and isn't {newEnergyWithH}, the heuristic value is {heuristic(newState)}, found this solution at {time.strftime('%X')} ({int(time.time())})")

endTime = time.perf_counter()
print(f"Took {endTime - startTime} seconds")
