grid = []
risk = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        grid.append([])
        for item, in line[:-1]:
            if line=="": continue
            grid[-1].append(int(item))


for y, line in enumerate(grid):
    for x, item in enumerate(line):
        surrounding = []
        if y > 0: surrounding.append(grid[y-1][x])
        if x > 0: surrounding.append(line[x-1])
        if y < len(grid) - 1: surrounding.append(grid[y+1][x])
        if x < len(line) - 1: surrounding.append(line[x+1])

        if item < min(surrounding): risk+=1+item
print(f"The answer is {risk}")
        