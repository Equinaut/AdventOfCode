import copy

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hallway = y == 1
        self.sideroom = y != 1
        self.neighbours = set()

    def __repr__(self):
        return f"Node({self.x}, {self.y})"

positions = {}
startPositions = {}
finalPositions = {"A": 3, "B": 5, "C": 7, "D": 9}

with open("inputSmall.txt", "r") as file:
    lines = file.readlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line[:-1]):
            if char=="#" or char == " ": continue
            if char.isalpha():
                if char not in startPositions: startPositions[char] = []
                startPositions[char].append((x, y))
            positions[(x, y)] = Node(x, y)


for position in positions.values():
    x, y = position.x, position.y
    for offsetX, offsetY in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (x+offsetX, y+offsetY) in positions:
            positions[x, y].neighbours.add(positions[x+offsetX, y+offsetY])

finished = False
previousStates = set()

def findRoutes(amphipodPositions, energy = 0):
    global previousStates
    global finished
    if finished: return
    if energy > 12600: return

    # print("Now state")
    # printState(amphipodPositions)
    # print()
    # print(previousPositions)
    # print()
    if "".join(outputState(amphipodPositions)) == "##############...........####A#B#C#D######A#B#C#D################":
        finished = True
        print("FINISHED\n" *1000)
        return
    
    print("".join(outputState(amphipodPositions)))

    previousStates.add("".join(outputState(amphipodPositions)))

    for char in amphipodPositions:
        for i in range(0, len(amphipodPositions[char])):
            thisCharPosition = amphipodPositions[char][i]

            for newPosition in positions[thisCharPosition].neighbours:
                if isTaken(amphipodPositions, newPosition.x, newPosition.y): 
                    #print("Spot is taken", thisCharPosition, newPosition)
                    continue
                
                if newPosition.sideroom and positions[thisCharPosition].hallway:
                    if newPosition.x != finalPositions[char]: 
                        #print("Cant go here", char, thisCharPosition, newPosition, newPosition.sideroom)
                        continue

                newAmphipodPositions = copy.deepcopy(amphipodPositions)
                newAmphipodPositions[char][i] = (newPosition.x, newPosition.y)
                
                if "".join(outputState(newAmphipodPositions)) in previousStates: 
                    # print("Been here before")
                    continue
                
                newEnergy = 1
                if char == "B": newEnergy = 10
                elif char == "C": newEnergy = 100
                elif char == "D": newEnergy = 1000
                
                # print("Now state")
                # printState(amphipodPositions)
                # print("Next state")
                # printState(newAmphipodPositions)

                findRoutes(newAmphipodPositions, energy + newEnergy)

def isTaken(amphipodPositions, x, y):
    for char, amphiPods in amphipodPositions.items():
        for amphiPod in amphiPods:
            if (x, y) == amphiPod: return True
    return False

def printState(amphipodPositions):
    width = max([node.x for node in positions.values()]) + 2
    height = max([node.y for node in positions.values()]) + 2
    
    outputLines = [["#" for x in range(0, width)] for y in range(0, height)]
    for (x, y) in positions:
        outputLines[y][x] = "."

    for char in amphipodPositions:
        for i in range(0, len(amphipodPositions[char])):
            x, y = amphipodPositions[char][i]
            outputLines[y][x] = char

    for outputLine in outputLines:
        print("".join(outputLine))

def outputState(amphipodPositions):
    width = max([node.x for node in positions.values()]) + 2
    height = max([node.y for node in positions.values()]) + 2

    outputLines = [["#" for x in range(0, width)] for y in range(0, height)]
    for (x, y) in positions:
        outputLines[y][x] = "."

    for char in amphipodPositions:
        for i in range(0, len(amphipodPositions[char])):
            x, y = amphipodPositions[char][i]
            outputLines[y][x] = char

    return ["".join(i) for i in outputLines]
findRoutes(startPositions)