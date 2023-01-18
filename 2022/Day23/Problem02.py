elveLocations = dict()
elfNumber = 0

with open("input.txt") as file:
    text = file.readlines()
    for y in range(0, len(text)):
        for x in range(0, len(text[y][:-1])):
            if text[y][x] == "#": 
                elveLocations[elfNumber] = (x, y)
                elfNumber += 1

def doRound(elveLocations, directions):
    proposedLocationsByElf = dict()
    allProposedLocations = set()
    failedLocations = set()
    filledLocations = set(elveLocations.values())

    for i in elveLocations:
        elfLocation = elveLocations[i]
        attemptedToMove = False
        if hasNeighbours(elfLocation, filledLocations):
            for direction in directions:
                if shouldMove(elfLocation, direction, filledLocations):
                    newLocation = getNewLocation(elfLocation, direction)
                    if newLocation in allProposedLocations: failedLocations.add(newLocation)

                    proposedLocationsByElf[i] = newLocation
                    allProposedLocations.add(newLocation)

                    attemptedToMove = True
                    break
        if not attemptedToMove:
            proposedLocationsByElf[i] = elveLocations[i]
            allProposedLocations.add(elveLocations[i])
    
    newLocations = {i: (proposedLocation if proposedLocation not in failedLocations else elveLocations[i]) for i, proposedLocation in proposedLocationsByElf.items()}
    elfMoved = False
    
    for i in elveLocations:
        if elveLocations[i] != newLocations[i]: elfMoved = True

    return newLocations, elfMoved

def hasNeighbours(elfLocation, filledLocations):
    anyNeighbours = False
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0: continue
            if (elfLocation[0] + x, elfLocation[1] + y) in filledLocations: 
                anyNeighbours = True
    return anyNeighbours

def shouldMove(elfLocation, direction, filledLocations):
    if direction == "N": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + i, elfLocation[1] - 1) for i in (-1, 0, 1))])
    elif direction == "S": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + i, elfLocation[1] + 1) for i in (-1, 0, 1))])
    elif direction == "E": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + 1, elfLocation[1] + i) for i in (-1, 0, 1))])
    elif direction == "W": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] - 1, elfLocation[1] + i) for i in (-1, 0, 1))])
    else: return False

def getNewLocation(elfLocation, direction):
    if direction == "N": return (elfLocation[0], elfLocation[1] - 1)
    elif direction == "S": return (elfLocation[0], elfLocation[1] + 1)
    elif direction == "E": return (elfLocation[0] + 1, elfLocation[1])
    elif direction == "W": return (elfLocation[0] - 1, elfLocation[1])
    else: return None

directions = ["N", "S", "W", "E"]
elfMoved = True
i = 0
while elfMoved:
    elveLocations, elfMoved = doRound(elveLocations, directions)
    directions = directions[1:] + directions[:1]
    i += 1

answer = i
print(f"The answer is {answer}")