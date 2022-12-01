grid = []
#1 = >
#2 = v

with open("inputtest.txt", "r") as file:
    for line in file.readlines():
        grid.append([])
        for item in line[:-1]:
            if item==">": grid[-1].append(1)
            elif item == "v": grid[-1].append(2)
            else: grid[-1].append(0)

def moveEast():
    canMove = []
    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            if item!= 1: continue
            if grid[y][(x+1)%len(line)]==0: canMove.append((x,y))

    for x, y in canMove:
        grid[y][x] = 0
        grid[y][(x+1)%len(grid[0])] = 1
    return len(canMove) > 0
def moveSouth():
    canMove = []
    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            if item!=2: continue
            if grid[(y+1)%len(grid)][x]==0: canMove.append((x,y))

    for x, y in canMove:
        grid[y][x] = 0
        grid[(y+1)%len(grid)][x] = 2
    return len(canMove) >0

for line in grid:
        for item in line:
            if item==0: print(".", end="")
            elif item==1: print(">", end="")
            elif item==2: print("v", end="")
        print()
i=0

couldMove = True
while couldMove:
    if i%100==0: print(i)
    couldMoveEast = moveEast()
    couldMoveSouth = moveSouth()
    i+=1
    if not (couldMoveEast or couldMoveSouth): couldMove=False
    # print("\n\n")
    # for line in grid:
    #     for item in line:
    #         if item==0: print(".", end="")
    #         elif item==1: print(">", end="")
    #         elif item==2: print("v", end="")
    #     print()

print(f"The answer is {i}")