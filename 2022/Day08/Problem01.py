grid = dict()

# Load file into dictionary object, in the form of (x,y): height
with open("input.txt") as file:
    for j, line in enumerate(file.readlines()):
        for i, height in enumerate(line[:-1]):
            grid[(i, j)] = int(height)
    height = i
    width = j

def visible(actualX, actualY):
    value = grid[(actualX, actualY)]
    if all([grid[x, actualY] < value for x in range(0, actualX)]): return True
    if all([grid[actualX, y] < value for y in range(0, actualY)]): return True
    if all([grid[x, actualY] < value for x in range(actualX + 1, width + 1)]): return True
    if all([grid[actualX, y] < value for y in range(actualY + 1, width + 1)]): return True

answer = 0

for (x, y) in grid:
    if visible(x, y): answer += 1

print(f"The answer is {answer}")