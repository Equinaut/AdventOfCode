walls = set()
rowRanges = dict()
colRanges = dict()
currentPosition, currentDirection = None, "R"

with open("input.txt") as file:
    gridText, path = file.read()[:-1].split("\n\n")
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

while (instruction := getInstruction(path)):
    if instruction == "R":
        currentDirection = {"R": "D", "D": "L", "L": "U", "U": "R"}[currentDirection]
        continue
    elif instruction == "L":
        currentDirection = {"R": "U", "U": "L", "L": "D", "D": "R"}[currentDirection]
        continue

    for i in range(0, instruction):
        # Wrapping
        if currentDirection == "R" and currentPosition[0] >= rowRanges[currentPosition[1]][1]: # Wrap right
            newPosition = (rowRanges[currentPosition[1]][0], currentPosition[1])
        elif currentDirection == "L" and currentPosition[0] <= rowRanges[currentPosition[1]][0]: # Wrap left
            newPosition = (rowRanges[currentPosition[1]][1], currentPosition[1])

        elif currentDirection == "D" and currentPosition[1] >= colRanges[currentPosition[0]][1]: # Wrap down
            newPosition = (currentPosition[0], colRanges[currentPosition[0]][0])
        elif currentDirection == "U" and currentPosition[1] <= colRanges[currentPosition[0]][0]: # Wrap up
            newPosition = (currentPosition[0], colRanges[currentPosition[0]][1])

        else:
            # Normal movement
            if currentDirection == "R": newPosition = (currentPosition[0] + 1, currentPosition[1])
            if currentDirection == "L": newPosition = (currentPosition[0] - 1, currentPosition[1])
            if currentDirection == "U": newPosition = (currentPosition[0], currentPosition[1] - 1)
            if currentDirection == "D": newPosition = (currentPosition[0], currentPosition[1] + 1)

        if newPosition in walls: break
        currentPosition = newPosition

x, y = currentPosition

answer = 1000 * (y + 1) + 4 * (x + 1) + {"R": 0, "D": 1, "L": 2, "U": 3}[currentDirection]
print(f"The answer is {answer}")