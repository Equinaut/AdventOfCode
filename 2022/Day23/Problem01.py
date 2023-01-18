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
        for direction in directions:
            if shouldMove(i, elveLocations, direction, filledLocations):
                newLocation = getNewLocation(i, elveLocations, direction)
                if newLocation in allProposedLocations: failedLocations.add(newLocation)

                proposedLocationsByElf[i] = newLocation
                allProposedLocations.add(newLocation)

                break
        else:
            proposedLocationsByElf[i] = elveLocations[i]
            allProposedLocations.add(elveLocations[i])
    
    return {i: (proposedLocation if proposedLocation not in failedLocations else elveLocations[i]) for i, proposedLocation in proposedLocationsByElf.items()}

def shouldMove(elveNumber, elveLocations, direction, filledLocations):
    elfLocation = elveLocations[elveNumber]

    anyNeighbours = False
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0: continue
            if (elfLocation[0] + x, elfLocation[1] + y) in filledLocations: 
                anyNeighbours = True
    if not anyNeighbours: return False

    if direction == "N": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + i, elfLocation[1] - 1) for i in (-1, 0, 1))])
    elif direction == "S": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + i, elfLocation[1] + 1) for i in (-1, 0, 1))])
    elif direction == "E": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] + 1, elfLocation[1] + i) for i in (-1, 0, 1))])
    elif direction == "W": return all([newLoc not in filledLocations for newLoc in ((elfLocation[0] - 1, elfLocation[1] + i) for i in (-1, 0, 1))])
    else:
        return False

def getNewLocation(elfNumber, elveLocations, direction):
    if direction not in "NSEW": return
    if direction == "N": return (elveLocations[elfNumber][0], elveLocations[elfNumber][1] - 1)
    if direction == "S": return (elveLocations[elfNumber][0], elveLocations[elfNumber][1] + 1)
    if direction == "E": return (elveLocations[elfNumber][0] + 1, elveLocations[elfNumber][1])
    if direction == "W": return (elveLocations[elfNumber][0] - 1, elveLocations[elfNumber][1])

def countEmpty(elveLocations):
    return (1 + max(y for x, y in elveLocations.values()) - min(y for x, y in elveLocations.values())) * (1 + max(x for x, y in elveLocations.values()) - min(x for x, y in elveLocations.values())) - len(elveLocations.values())

directions = ["N", "S", "W", "E"]
for i in range(10):
    elveLocations = doRound(elveLocations, directions)
    directions = directions[1:] + directions[:1]

answer = countEmpty(elveLocations)
print(f"The answer is {answer}")