import copy
import time

startTime = time.perf_counter()

positions = [(1,1),
             (2, 1),
             (3, 1),
             (4, 1),
             (5, 1),
             (6, 1),
             (7, 1),
             (8, 1),
             (9, 1),
             (10, 1),
             (11, 1),
             (3, 2),
             (3, 3),
             (5, 2),
             (5, 3),
             (7, 2),
             (7, 3),
             (9, 2),
             (9, 3)]

startState = [
    ("A", 3, 2),
    ("A", 7, 3),
    ("B", 7, 2),
    ("B", 9, 2),
    ("C", 5, 2),
    ("C", 9, 3),
    ("D", 3, 3),
    ("D", 5, 3)
]

def nextState(currentPosition, currentPositions):
    possiblePositions = set()

    amphipodType, x, y = currentPosition
    myRoom = {"A": 3, "B": 5, "C": 7, "D": 9}[amphipodType]

    if amphipodType == "D" and (x < 3 or x > 9): return set()

    if y == 1: #In hallway
        # Places you can move in the hallway
        leftBound, rightBound = 0, 12
        for item in currentPositions:
            if item == currentPosition: continue
            if item[2] != 1: continue
            if item[1] > leftBound and item[1] < x: leftBound = item[1]
            if item[1] < rightBound and item[1] > x: rightBound = item[1]
        

        # Can you enter your room?
        enterOwnRoom = True
        ownRoomEmpty = True
        if myRoom <= leftBound or myRoom >= rightBound: 
            enterOwnRoom = False
            ownRoomEmpty = False

        for item in currentPositions:
            if item == currentPosition: continue
            if item[0] == amphipodType: 
                if item[1] == myRoom: ownRoomEmpty = False
                continue
            if item[1] == myRoom:
                ownRoomEmpty = False
                enterOwnRoom = False
        
        if ownRoomEmpty: possiblePositions.add((myRoom, 3))
        elif enterOwnRoom: possiblePositions.add((myRoom, 2))
    

        possiblePositions2 = set()
        for possiblePosition in possiblePositions:
            distance = 0
            distance += abs(x - possiblePosition[0])
            distance += y - 1
            distance += possiblePosition[1] - 1
            if amphipodType == "B": distance *= 10
            elif amphipodType == "C": distance *= 100
            elif amphipodType == "D": distance *= 1000

            possiblePositions2.add((*possiblePosition, distance))

        return possiblePositions2

    if y == 2: #In doorway
        roomComplete = False
        if x == myRoom:
            for item in currentPositions:
                if item == currentPosition: continue
                if item[0] == amphipodType:
                    if item[1] == x:
                        roomComplete = True
                        break

        if roomComplete: return set()

        leftBound, rightBound = 0, 12
        for item in currentPositions:
            if item == currentPosition: continue
            if item[2] != 1: continue
            if item[1] > leftBound and item[1] < x: leftBound = item[1]
            if item[1] < rightBound and item[1] > x: rightBound = item[1]
        
        for x2 in range(leftBound + 1, rightBound):
            if x2 in {3, 5, 7, 9}: continue
            possiblePositions.add((x2, 1))

        possiblePositions2 = set()
        for possiblePosition in possiblePositions:
            distance = 0
            distance += abs(x - possiblePosition[0])
            distance += y - 1
            distance += possiblePosition[1] - 1
            if amphipodType == "B": distance *= 10
            elif amphipodType == "C": distance *= 100
            elif amphipodType == "D": distance *= 1000
            
            possiblePositions2.add((*possiblePosition, distance))

        return possiblePositions2

    #In bottom of sideroom

    for item in currentPositions:
        if item == currentPosition: continue

        if item[2] == 2 and item[1] == x: return set()
    
    roomComplete = False
    if x == myRoom:
        for item in currentPositions:
            if item == currentPosition:
                continue
            if item[0] == amphipodType:
                if item[1] == x:
                    roomComplete = True
                    break

    if roomComplete:
        return set()

    leftBound, rightBound = 0, 12
    for item in currentPositions:
        if item == currentPosition:
            continue
        if item[2] != 1:
            continue
        if item[1] > leftBound and item[1] < x:
            leftBound = item[1]
        if item[1] < rightBound and item[1] > x:
            rightBound = item[1]

    for x2 in range(leftBound + 1, rightBound):
        if x2 in {3, 5, 7, 9}:
            continue
        possiblePositions.add((x2, 1))

    possiblePositions2 = set()
    for possiblePosition in possiblePositions:
        distance = 0
        distance += abs(x - possiblePosition[0])
        distance += y - 1
        distance += possiblePosition[1] - 1
        if amphipodType == "B": distance *= 10
        elif amphipodType == "C": distance *= 100
        elif amphipodType == "D": distance *= 1000
        
        possiblePositions2.add((*possiblePosition, distance))

    return possiblePositions2


def allPossibleStates(currentState):
    possibleStates = []
    for i, currentAmphipod in enumerate(currentState):
        newPositions = nextState(currentAmphipod, currentState)
        for newPosition in newPositions:
            newState = copy.deepcopy(currentState)
            newState[i] = (newState[i][0], newPosition[0], newPosition[1])
            possibleStates.append((newState, newPosition[2]))
    return possibleStates


def outputState(amphipodPositions):
    width = 13
    height = 5

    outputLines = [["#" for x in range(0, width)] for y in range(0, height)]
    for (x, y) in positions:
        outputLines[y][x] = "."
    print
    for amphipod in amphipodPositions:
        outputLines[amphipod[2]][amphipod[1]] = amphipod[0]

    return ["".join(i) for i in outputLines]


queue = []
previousStates = set()

queue.append((0, startState))

def addToQueue(newEnergy, state):
    if len(queue) == 0 or newEnergy > queue[-1][0]:
        queue.append((newEnergy, state))
        return
    if newEnergy < queue[0][0]: 
        queue.insert(0, (newEnergy, state))
        return

    i = 0

    while newEnergy > queue[i][0] and i + 1 < len(queue): i+=1
    queue.insert(i, (newEnergy, state))

def finished(item):
    for i in item:
        myRoom = {"A": 3, "B": 5, "C": 7, "D": 9}[i[0]]
        if i[1] != myRoom: return False
        if i[2] == 1: return False
    return True

while len(queue) > 0:
    currentEnergy, currentItem = queue.pop(0)
    #print(currentItem)
    if str(currentItem) in previousStates: continue
    previousStates.add(str(currentItem))

    if finished(currentItem):
        print(f"The answer is {currentEnergy}")
        break
    
    if len(queue) % 20==1: print(len(queue), currentEnergy)
    
    newStates = allPossibleStates(currentItem)

    for state, energy in newStates:
        addToQueue(currentEnergy + energy, state)


endTime = time.perf_counter()
print(f"Took {endTime - startTime} seconds to finish")