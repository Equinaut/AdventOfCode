UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
UP_DOWN, RIGHT_LEFT = 0, 1
EMPTY, BLOCKED, VISITED = 0, 1, 2

def getOriginalPath(grid, pos):
    # Trace the path walked when no extra obstacles are present
    # This is the set of positions that must be tested with a new obstacle
    path = list()

    direction = UP
    while True:
        nextPos = None
        # Add newly discovered positions to path list
        if (grid[pos[1]][pos[0]] == EMPTY):
            path.append(pos)
            grid[pos[1]][pos[0]] = VISITED

        if direction == UP: nextPos = (pos[0], pos[1] - 1)
        elif direction == RIGHT: nextPos = (pos[0] + 1, pos[1])
        elif direction == DOWN: nextPos = (pos[0], pos[1] + 1)
        elif direction == LEFT: nextPos = (pos[0] - 1, pos[1])

        # Finish when out of bounds
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): break

        # Turn when an obstacle is encountered
        if grid[nextPos[1]][nextPos[0]] == BLOCKED:
            direction = (direction + 1) % 4
            continue

        pos = nextPos
    return path

def searchForCycle(grid, pos, nextPositions, extraObstacle = None):
    direction = UP
    seenPositions = [set(), set(), set(), set()]

    while True:
        nextX, nextY = pos[0], pos[1]
        
        # If a previously seen position is discovered, then a loop is present
        if pos in seenPositions[direction]: return True
        seenPositions[direction].add(pos)

        # Go to square before next obstacle
        if direction == UP or direction == DOWN: nextY = nextPositions[UP_DOWN][pos[1]][pos[0]][direction >> 1]
        elif direction == RIGHT or direction == LEFT: nextX = nextPositions[RIGHT_LEFT][pos[1]][pos[0]][direction >> 1]

        # If extra obstacle is between old position and next normal obstacle, then the 
        # extra obstacle will be used instead
        if extraObstacle is not None:
            if (direction == UP and extraObstacle[0] == pos[0] and extraObstacle[1] < pos[1] and extraObstacle[1] >= nextY):
                nextY = extraObstacle[1] + 1
            elif (direction == RIGHT and extraObstacle[1] == pos[1] and extraObstacle[0] > pos[0] and extraObstacle[0] <= nextX):
                nextX = extraObstacle[0] - 1
            elif (direction == DOWN and extraObstacle[0] == pos[0] and extraObstacle[1] > pos[1] and extraObstacle[1] <= nextY):
                nextY = extraObstacle[1] - 1
            elif (direction == LEFT and extraObstacle[1] == pos[1] and extraObstacle[0] < pos[0] and extraObstacle[0] >= nextX):
                nextX = extraObstacle[0] + 1

        # Check for out of bounds
        if nextX < 0 or nextY < 0 or nextX >= len(grid[0]) or nextY >= len(grid): return False
        
        pos = (nextX, nextY)
        direction = (direction + 1) % 4

def makeFastGrid(grid, nextPositions):
    # Scans the grid, and makes lists that store the location of the next obstacle in every direction
    # from every square on the board
    for y in range(0, len(grid)):
        last = len(grid[0]) + 1
        for x in range(len(grid[0]) - 1, 0, -1):
            if grid[y][x] == BLOCKED: last = x - 1
            nextPositions[RIGHT_LEFT][y][x][RIGHT >> 1] = last

        last = -1
        for x in range(0, len(grid[0])):
            if grid[y][x] == BLOCKED: last = x + 1
            nextPositions[RIGHT_LEFT][y][x][LEFT >> 1] = last

    for x in range(0, len(grid[0])):        
        last = -1
        for y in range(0, len(grid)):
            if grid[y][x] == BLOCKED: last = y + 1
            nextPositions[UP_DOWN][y][x][UP >> 1] = last

        last = len(grid) + 1
        for y in range(len(grid) - 1, 0, -1):
            if grid[y][x] == BLOCKED: last = y - 1
            nextPositions[UP_DOWN][y][x][DOWN >> 1] = last

def main():
    ans = 0
    with open("input.txt") as file:
        lines = file.readlines()
        width = len(lines[0]) -1 
        height = len(lines)
        grid = [[EMPTY] * width for _ in range(height)]

    pos = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^": pos = (x, y)
            elif c == "#": grid[y][x] = BLOCKED

    nextPositions = [
        [[[0, 0] for a in range(width)] for _ in range(height)],
        [[[0, 0] for a in range(height)] for _ in range(width)],
    ]
    makeFastGrid(grid, nextPositions)

    for x, y in getOriginalPath(grid, pos):
        if (x, y) == pos: continue
        if grid[y][x] == BLOCKED: continue
        if searchForCycle(grid, pos, nextPositions, (x, y)): ans += 1
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")