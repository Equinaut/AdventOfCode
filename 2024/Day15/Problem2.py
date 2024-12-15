WALL = 1
EMPTY = 0
BOX_LEFT = 2 
BOX_RIGHT = 3

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
            elif c == BOX_LEFT: print("[", end="")
            elif c == BOX_RIGHT: print("]", end="")
        print()

# Updates the grid with a new position
# returns the new position of the robot
def applyMovement(grid, botPos, movement):
    res = canPush(grid, botPos, movement)
    if res == False: return botPos
    if res == True:
        applyMovementToGrid(grid, botPos, movement)
        if movement == NORTH: return (botPos[0], botPos[1] - 1)
        if movement == EAST: return (botPos[0] + 1, botPos[1])
        if movement == SOUTH: return (botPos[0], botPos[1] + 1)
        if movement == WEST: return (botPos[0] - 1, botPos[1])

# Updates the grid with a new movement
def applyMovementToGrid(grid, pushPos, movement):
    x, y = pushPos
    if movement == NORTH:
        if grid[y - 1][x] == BOX_LEFT:
            applyMovementToGrid(grid, (pushPos[0], pushPos[1] - 1), movement)
            applyMovementToGrid(grid, (pushPos[0] + 1, pushPos[1] - 1), movement)
        if grid[y - 1][x] == BOX_RIGHT:
            applyMovementToGrid(grid, (pushPos[0] - 1, pushPos[1] - 1), movement)
            applyMovementToGrid(grid, (pushPos[0], pushPos[1] - 1), movement)
        grid[y - 1][x] = grid[y][x]
        grid[y][x] = EMPTY
    
    elif movement == SOUTH:
        if grid[y + 1][x] == BOX_LEFT:
            applyMovementToGrid(grid, (pushPos[0], pushPos[1] + 1), movement)
            applyMovementToGrid(grid, (pushPos[0] + 1, pushPos[1] + 1), movement)
        if grid[y + 1][x] == BOX_RIGHT:
            applyMovementToGrid(grid, (pushPos[0] - 1, pushPos[1] + 1), movement)
            applyMovementToGrid(grid, (pushPos[0], pushPos[1] + 1), movement)
        grid[y + 1][x] = grid[y][x]
        grid[y][x] = EMPTY

    elif movement == EAST:
        if grid[y][x + 1] == BOX_LEFT:
            applyMovementToGrid(grid, (pushPos[0] + 1, pushPos[1]), movement)
        if grid[y][x + 1] == BOX_RIGHT:
            applyMovementToGrid(grid, (pushPos[0] + 1, pushPos[1]), movement)
        grid[y][x + 1] = grid[y][x]
        grid[y][x] = EMPTY

    elif movement == WEST:
        if grid[y][x - 1] == BOX_LEFT:
            applyMovementToGrid(grid, (pushPos[0] - 1, pushPos[1]), movement)
        if grid[y][x - 1] == BOX_RIGHT:
            applyMovementToGrid(grid, (pushPos[0] - 1, pushPos[1]), movement)
        grid[y][x - 1] = grid[y][x]
        grid[y][x] = EMPTY

# Checks if a movement is possible
def canPush(grid, pushPos, movement):
    if movement == WEST:
        x, y = pushPos[0] - 1, pushPos[1]
        if grid[y][x] == EMPTY: return True
        if grid[y][x] == WALL: return False
        if grid[y][x] == BOX_RIGHT or grid[y][x] == BOX_LEFT: 
            return canPush(grid, (x, y), movement)
    elif movement == EAST:
        x, y = pushPos[0] + 1, pushPos[1]
        if grid[y][x] == EMPTY: return True
        if grid[y][x] == WALL: return False
        if grid[y][x] == BOX_RIGHT or grid[y][x] == BOX_LEFT: 
            return canPush(grid, (x, y), movement)
    elif movement == NORTH:
        x, y = pushPos[0], pushPos[1] - 1
        if grid[y][x] == EMPTY: return True
        if grid[y][x] == WALL: return False
        if grid[y][x] == BOX_RIGHT: 
            x -= 1
        if grid[y][x] == BOX_LEFT: 
            res1 = canPush(grid, (x, y), movement)
            res2 = canPush(grid, (x + 1, y), movement)
            return res1 and res2
    elif movement == SOUTH:
        x, y = pushPos[0], pushPos[1] + 1
        if grid[y][x] == EMPTY: return True
        if grid[y][x] == WALL: return False
        if grid[y][x] == BOX_RIGHT: 
            x -= 1
        if grid[y][x] == BOX_LEFT: 
            res1 = canPush(grid, (x, y), movement)
            res2 = canPush(grid, (x + 1, y), movement)
            return res1 and res2
    return True

def main():
    grid = []
    movements = []
    botPos = None

    with open("input.txt") as file:
        line = None
        y = 0
        while line != "\n":
            line = file.readline()
            grid.append([EMPTY] * (len(line) - 1) * 2)
            for x in range(0, len(line) - 1):
                if line[x] == "O": 
                    grid[-1][x * 2 + 0] = BOX_LEFT
                    grid[-1][x * 2 + 1] = BOX_RIGHT
                elif line[x] == "#": 
                    grid[-1][x * 2 + 0] = WALL
                    grid[-1][x * 2 + 1] = WALL
                elif line[x] == "@": 
                    botPos = (x * 2, y)
            y += 1
        while line:
            line = file.readline()
            for c in line:
                if c == "<": movements.append(WEST)
                elif c == ">": movements.append(EAST)
                elif c == "^": movements.append(NORTH)
                elif c == "v": movements.append(SOUTH)

    for movement in movements:
        botPos = applyMovement(grid, botPos, movement)

    ans = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == BOX_LEFT:
                ans += y * 100 + x
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")