WALL = 1
EMPTY = 0
BOX = 2 

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def printGrid(grid, botPos):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if (x, y) == botPos: print("@", end="")
            elif c == WALL: print("#", end="")
            elif c == EMPTY: print(".", end="")
            elif c == BOX: print("O", end="")
            else: print("£", end="")
        print()

def applyMovement(grid, botPos, movement):
    boxesToMove = []
    if movement == WEST: offset = (-1, 0)
    if movement == EAST: offset = (1, 0)
    if movement == SOUTH: offset = (0, 1)
    if movement == NORTH: offset = (0, -1)
    x, y = botPos[0] + offset[0], botPos[1] + offset[1]
    while grid[y][x] != EMPTY:
        if grid[y][x] == WALL: return botPos
        elif grid[y][x] == BOX: boxesToMove.append((x, y))
        x += offset[0]
        y += offset[1]
    if len(boxesToMove):
        grid[boxesToMove[0][1]][boxesToMove[0][0]] = EMPTY
        grid[boxesToMove[-1][1] + offset[1]][boxesToMove[-1][0] + offset[0]] = BOX
    return (botPos[0] + offset[0], botPos[1] + offset[1])
    
def main():
    grid = []
    movements = []
    botPos = None

    with open("input.txt") as file:
        line = None
        y = 0
        while line != "\n":
            line = file.readline()
            grid.append([EMPTY] * (len(line) - 1))
            for x in range(0, len(line) - 1):
                if line[x] == "O": grid[-1][x] = BOX
                if line[x] == "#": grid[-1][x] = WALL
                if line[x] == "@": botPos = (x, y)
            y += 1

        while line:
            line = file.readline()
            for c in line:
                if c == "<": movements.append(WEST)
                if c == ">": movements.append(EAST)
                if c == "^": movements.append(NORTH)
                if c == "v": movements.append(SOUTH)

    for movement in movements:
        botPos = applyMovement(grid, botPos, movement)

    ans = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == BOX:
                ans += y * 100 + x
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")