import heapq

EMPTY = 0
WALL = 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solveGrid(grid, start, cheat):
    if cheat is None:positions = [(0, start, (start, ))]
    else: positions = [(0, start, None)]

    visited = set()
    previous = dict()
    distances = dict()
    while positions:
        currentDist, pos, path = heapq.heappop(positions)
        if pos in visited: continue
        visited.add(pos)

        if pos not in distances: distances[pos] = currentDist
        else: distances[pos] = min(currentDist, distances[pos])

        for d in directions:
            nextPos = (pos[0] + d[0], pos[1] + d[1])
            if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): continue
            if (grid[nextPos[1]][nextPos[0]] != EMPTY): continue
            previous[nextPos] = pos
            newPath = None if path is None else (*path, nextPos)
            heapq.heappush(positions, (currentDist + 1, nextPos, newPath))

        if cheat is not None and pos == cheat[0]:
            newPath = None if path is None else (*path, nextPos)
            heapq.heappush(positions, (currentDist + 2, cheat[1], newPath))
    
    return distances


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        width, height = (len(lines[0]) - 1, len(lines))

        grid = [[EMPTY] * width for _ in range(height)]

        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                if c == "#": grid[y][x] = WALL
                else: grid[y][x] = EMPTY
                if c == "S": start = (x, y)
                if c == "E": end = (x, y)

        
        startDist = solveGrid(grid, start, None)
        endDist = solveGrid(grid, end, None)

        normalDist = startDist[end]
        values = dict()

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if x % 20 == 0: print(x, y)
                cheatStart = (x, y)
                if grid[cheatStart[1]][cheatStart[0]] != EMPTY: continue

                for d in directions:
                    mid = (x + d[0], y + d[1])
                    cheatEnd = (x + d[0] + d[0], y + d[1] + d[1])
                    if cheatEnd[0] < 0 or cheatEnd[1] < 0 or cheatEnd[0] >= len(grid) or cheatEnd[1] >= len(grid): continue
                    if grid[cheatEnd[1]][cheatEnd[0]] != EMPTY: continue

                    l1 = startDist[cheatStart]
                    l2 = endDist[cheatEnd]
                    n = l1 + l2 + 2

                    l3 = normalDist - n
                    # l = normalTime - solveGrid(grid, start, end, (x, y))
                    if l3 <= 0: continue
                    if l3 not in values: values[l3] = 0
                    values[l3] += 1

    print("Cheats")
    print(normalDist)
    ans = 0        
    for l in sorted(values):
        print(l, values[l])
        if l >= 100: ans += values[l]

    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")