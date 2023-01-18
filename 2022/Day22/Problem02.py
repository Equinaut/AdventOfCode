walls = set()

rowRanges = dict()
colRanges = dict()

lastDirection = dict()
currentPosition, currentDirection = None, "R"

with open("input.txt") as file:
    text = file.read()
    gridText, path = text[:-1].split("\n\n")
    path = list(path)
    gridText = gridText.split("\n")
    for y in range(0, len(gridText)):
        minX = maxX = None
        for x in range(0, len(gridText[y])):
            if gridText[y][x] == "#": walls.add((x, y))
            if gridText[y][x] in ".#":
                if minX is None: minX = x
                if maxX is None or x > maxX: maxX = x
            if y == 0 and currentPosition is None and gridText[y][x] == ".":
                currentPosition = (x, y)

        rowRanges[y] = (minX, maxX)

for x in range(0, max(rowRanges.values(), key = lambda r: r[1])[1] + 1):
    minY = maxY = None
    for y in range(0, len(gridText)):
        if (len(gridText[y]) > x) and gridText[y][x] in ".#":
            if minY is None: minY = y
            if maxY is None or y > maxY: maxY = y
    colRanges[x] = (minY, maxY)

def getInstruction(path):
    if len(path) == 0: return None
    if path[0].isalpha(): return path.pop(0)
    
    i = 0
    while i < len(path) and path[i].isnumeric(): i += 1
    result = int("".join(path[:i]))
    
    del path[:i]
    return result

while (instruction:= getInstruction(path)):
    if instruction == "R":
        currentDirection = {"R": "D", "D": "L", "L": "U", "U": "R"}[currentDirection]
        continue
    if instruction == "L":
        currentDirection = {"R": "U", "U": "L", "L": "D", "D": "R"}[currentDirection]
        continue

    for i in range(0, instruction):
        lastDirection[currentPosition] = currentDirection
        newDirection = currentDirection
        x, y = currentPosition
        if currentDirection == "R" and currentPosition[0] >= rowRanges[currentPosition[1]][1]: # Wrap right
            if y < 50: newDirection, newPosition = "L", (99, 149 - y)
            elif y < 100: newDirection, newPosition = "U", (y + 50, 49)
            elif y < 150: newDirection, newPosition = "L", (149, 149 - y)
            elif y < 200: newDirection, newPosition = "U", (y - 100, 149)

        elif currentDirection == "L" and currentPosition[0] <= rowRanges[currentPosition[1]][0]: # Wrap left
            if y < 50: newDirection, newPosition = "R", (0, 149 - y)
            elif y < 100: newDirection, newPosition = "D", (y - 50, 100)
            elif y < 150: newDirection, newPosition = "R", (50, 149 - y)
            elif y < 200: newDirection, newPosition = "D", (y - 100, 0)

        elif currentDirection == "D" and currentPosition[1] >= colRanges[currentPosition[0]][1]: # Wrap down
            if x < 50: newDirection, newPosition = "D", (x + 100, 0)
            elif x < 100: newDirection, newPosition = "L", (49, x + 100)
            elif x < 150: newDirection, newPosition = "L", (99, x - 50)

        elif currentDirection == "U" and currentPosition[1] <= colRanges[currentPosition[0]][0]: # Wrap up
            if x < 50: newDirection, newPosition = "R", (50, x + 50)
            elif x < 100: newDirection, newPosition = "R", (0, x + 100)
            elif x < 150: newDirection, newPosition = "U", (x - 100, 199)

        else:
            # Normal movement
            if currentDirection == "R": newPosition = (currentPosition[0] + 1, currentPosition[1])
            elif currentDirection == "L": newPosition = (currentPosition[0] - 1, currentPosition[1])
            elif currentDirection == "U": newPosition = (currentPosition[0], currentPosition[1] - 1)
            elif currentDirection == "D": newPosition = (currentPosition[0], currentPosition[1] + 1)

        if newPosition in walls: break
        currentDirection, currentPosition = newDirection, newPosition

x, y = currentPosition
answer = 1000 * (y + 1) + 4 * (x + 1) + {"R": 0, "D": 1, "L": 2, "U": 3}[currentDirection]
print(f"The answer is {answer}")