import heapq

EMPTY = 0
WALL = 1

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solveGrid(grid, start):
    positions = [(0, start)]

    distances = dict()
    while positions:
        currentDist, pos = heapq.heappop(positions)
        if pos in distances: continue
        distances[pos] = currentDist

        for d in directions:
            nextPos = (pos[0] + d[0], pos[1] + d[1])

            if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): 
                continue
            
            if (grid[nextPos[1]][nextPos[0]] != EMPTY): continue

            heapq.heappush(positions, (currentDist + 1, nextPos))

    return distances


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        width, height = (len(lines[0]) - 1, len(lines))

        grid = [[EMPTY] * width for _ in range(height)]

        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                grid[y][x] = WALL if c == "#" else EMPTY

                if c == "S": start = (x, y)
                if c == "E": end = (x, y)
        
        startDist = solveGrid(grid, start)
        endDist = solveGrid(grid, end)

        normalDistance = startDist[end]

        ans = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                cheatStart = (x, y)
                if grid[cheatStart[1]][cheatStart[0]] != EMPTY: continue

                for xOff in range(-20, 21):
                    for yOff in range(-20, 21):
                        if abs(xOff) + abs(yOff) >= 21: continue

                        cheatEnd = (x + xOff, y + yOff)
                        if cheatEnd[0] < 0 or cheatEnd[1] < 0 or cheatEnd[0] >= len(grid) or cheatEnd[1] >= len(grid): continue
                        if grid[cheatEnd[1]][cheatEnd[0]] != EMPTY: continue

                        l1 = startDist[cheatStart]
                        l2 = endDist[cheatEnd]
                        n = l1 + l2 + abs(xOff) + abs(yOff)

                        if normalDistance - n >= 100: ans += 1
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")
