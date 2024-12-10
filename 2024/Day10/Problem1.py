def search(startPos, path, grid, startCounts):
    currentHeight = grid[path[-1][1]][path[-1][0]]
    if currentHeight == 9: startCounts[startPos].add(path[-1])

    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextPos = (path[-1][0] + d[0], path[-1][1] + d[1])

        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): continue

        newHeight = grid[nextPos[1]][nextPos[0]]
        if newHeight != currentHeight + 1: continue

        search(startPos, path + [nextPos], grid, startCounts)

def main():
    ans = 0
    with open("input.txt") as file:
        lines = file.readlines()
        grid = [[None] * (len(lines[0]) - 1) for _ in range(len(lines))]
        starts = []
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                if c == ".": continue
                grid[y][x] = int(c)
                if int(c) == 0: starts.append((x, y))

    counts = dict()
    for start in starts:
        counts[start] = set()
        search(start, [start], grid, counts)
        ans += len(counts[start])
            
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")