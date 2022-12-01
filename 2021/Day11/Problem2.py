grid = []
flashedThisStep = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        grid.append([])
        flashedThisStep.append([])
        for item in line[:-1]:
            grid[-1].append(int(item))
            flashedThisStep[-1].append(False)

def step():
    for y, line in enumerate(grid):
        for x in range(len(line)):
            flashedThisStep[y][x] = False


    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            grid[y][x] = item + 1
            if grid[y][x] == 10: flash(x, y)

    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            if item > 9: grid[y][x] = 0


def flash(x, y):
    flashedThisStep[y][x] = True
    for xOffset in range(-1, 2):
        for yOffset in range(-1, 2):
            if xOffset == 0 and yOffset == 0: continue
            if y + yOffset < 0 or y + yOffset >= len(grid): continue
            if x + xOffset < 0 or x + xOffset >= len(grid[y + yOffset]): continue
            
            grid[y + yOffset][x + xOffset] += 1
            if grid[y + yOffset][x + xOffset] == 10: flash(x + xOffset, y + yOffset)


def allFlashed(flashedThisTurn):
    allFlashed = True
    for line in flashedThisStep:
        for item in line:
            allFlashed = allFlashed and item
    return allFlashed

answer = 0

while not allFlashed(flashedThisStep):
    step()
    answer += 1

print(f"The answer is {answer}")