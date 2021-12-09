grid = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        grid.append([])
        for item, in line[:-1]:
            if line=="": continue
            grid[-1].append(int(item))

basins = [[None for _ in line] for line in grid]
basinId = 0
totalBasinAreaNow = 0
totalBasinArea = len(grid) * len(grid[0])

for y, line in enumerate(grid):
    for x, item in enumerate(line):
        if item==9:
            totalBasinArea -= 1
            continue
        left = right = up = down = None
        if y > 0: up = grid[y-1][x]
        if x > 0: left = line[x-1]
        if y < len(grid) - 1: down = grid[y+1][x]
        if x < len(line) - 1: right = line[x+1]
        surrounding = [left, right, up, down]    
        while None in surrounding: surrounding.remove(None)

        if left is not None and left < item: basins[y][x] = (y, x-1)
        elif right is not None and right < item: basins[y][x] = (y, x+1)
        elif up is not None and up < item: basins[y][x] = (y-1, x)
        elif down is not None and down < item: basins[y][x] = (y+1, x)
        elif item < min(surrounding): 
            basins[y][x] = basinId
            basinId +=1

totalBasinArea -= basinId

while totalBasinAreaNow < totalBasinArea:
    for y, line in enumerate(basins):
        for x, item in enumerate(line):
            if basins[y][x] is None: continue
            if type(basins[y][x]) != tuple: continue
            newY, newX = basins[y][x]

            basins[y][x] = basins[newY][newX]
            if type(basins[y][x]) != tuple:
                totalBasinAreaNow += 1

basinSizes = {i:0 for i in range(0, basinId)}

for line in basins:
    for item in line:
        if item is None: continue
        basinSizes[item] += 1

largest3 = list(basinSizes.values())
largest3.sort(reverse=True)
largest3 = largest3[:3]
answer = 1
for item in largest3: answer *= item

print(f"The answer is {answer}")