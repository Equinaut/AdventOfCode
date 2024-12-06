UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
EMPTY, BLOCKED, VISITED = 0, 1, 2

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
                if c == "#": grid[y][x] = BLOCKED

    direction = UP
    while True:
        nextPos = None
        if (grid[pos[1]][pos[0]] == EMPTY): 
            ans += 1
            grid[pos[1]][pos[0]] = VISITED
        
        if direction == UP: nextPos = (pos[0], pos[1] - 1)
        elif direction == RIGHT: nextPos = (pos[0] + 1, pos[1])
        elif direction == DOWN: nextPos = (pos[0], pos[1] + 1)
        elif direction == LEFT: nextPos = (pos[0] - 1, pos[1])

        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= width or nextPos[1] >= height: break

        if grid[nextPos[1]][nextPos[0]] == BLOCKED:
            direction = (direction + 1) % 4
            continue

        pos = nextPos
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")