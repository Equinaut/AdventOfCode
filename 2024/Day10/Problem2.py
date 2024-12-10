def search(lastPos, grid):
    currentHeight = grid[lastPos[1]][lastPos[0]]
    if currentHeight == 9: return 1
    count = 0
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextPos = (lastPos[0] + d[0], lastPos[1] + d[1])
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): continue
        newHeight = grid[nextPos[1]][nextPos[0]]

        if newHeight != currentHeight + 1: continue
        count += search(nextPos, grid)
    return count

def main():
    ans = 0
    with open("input.txt") as file:
        lines = file.readlines()
        grid = [[None] * (len(lines[0]) - 1) for _ in range(len(lines))]
        starts = list()
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                if c == ".": continue
                grid[y][x] = int(c)
                if grid[y][x] == 0: starts.append((x, y))

    ans = sum(search(start, grid) for start in starts)
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")