grid = []

steps = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        grid.append([])
        for item in line[:-1]:
            grid[-1].append(int(item))

def step():
    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            grid[y][x] = item + 1
            if grid[y][x] == 10: flash(x, y)

    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            if item > 9: grid[y][x] = 0

def flash(x, y):
    global steps
    steps += 1

    for xOffset in range(-1, 2):
        for yOffset in range(-1, 2):
            if xOffset == 0 and yOffset == 0: continue
            if y + yOffset < 0 or y + yOffset >= len(grid): continue
            if x + xOffset < 0 or x + xOffset >= len(grid[y + yOffset]): continue
            
            grid[y + yOffset][x + xOffset] += 1
            if grid[y + yOffset][x + xOffset] == 10: flash(x + xOffset, y + yOffset)

for i in range(0, 100): step()

print(f"The answer is {steps}")