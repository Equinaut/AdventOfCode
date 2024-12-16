import heapq

EMPTY = 0
WALL = 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def main():
    with open("input.txt") as file:
        lines = file.readlines()
        lastCornerByRow = [None] * len(lines)
        lastCornerByColumn = [None] * (len(lines[0]) - 1)
        start = end = None
        graph = dict()
        minDist = dict()

        # Process input to find the corners ( Paths where paths connect in multiple directions )
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                if c == "#": # Piece is a wall 
                    lastCornerByColumn[x] = None
                    lastCornerByRow[y] = None
                    continue

                if c == "S": start = (x, y) # Start position
                elif c == "E": end = (x, y) # End position
                hasNeighbours = [
                    lines[y + yOff][x + xOff] == "." and y + yOff < len(lines) and x + xOff < len(lines[0]) and x + xOff >= 0 and y + yOff >= 0
                    for xOff, yOff in directions
                ]
                
                if c != "." or any(hasNeighbours[i] and hasNeighbours[(i + 1) % 4] for i in range(0, 4)): 
                    # If piece is a corner piece then add it to the graph, and detect which corners are directly inline with it
                    minDist[(x, y)] = [None] * 4
                    graph[(x, y)] = [None] * 4

                    graph[x, y][WEST] = lastCornerByRow[y]
                    if lastCornerByRow[y] is not None:
                        graph[lastCornerByRow[y], y][EAST] = x

                    graph[x, y][NORTH] = lastCornerByColumn[x]
                    if lastCornerByColumn[x] is not None:
                        graph[x, lastCornerByColumn[x]][SOUTH] = y

                    lastCornerByRow[y] = x
                    lastCornerByColumn[x] = y

    # Start position, and start where the first move is a 180 degree rotation, as the rest of the program won't do two turns in a row
    queue = [
        (2000, start, WEST, (tuple(start), ), False),
        (0, start, EAST, (tuple(start), ), False),
    ]

    shortestPath = None
    paths = set()
    while queue:
        score, pos, dir, path, turnedLast = heapq.heappop(queue)
        if minDist[pos][dir] is not None and score > minDist[pos][dir]: continue
        else: minDist[pos][dir] = score

        if pos == end:
            if shortestPath is None or score == shortestPath:
                for i in range(1, len(path)):
                    paths.add((path[i - 1], path[i]))
                shortestPath = score
            else: break

        # Options for turning the corner
        if not turnedLast:
            heapq.heappush(queue, (score + 1000, pos, (dir + 1) % 4, path + (pos,), True))
            heapq.heappush(queue, (score + 1000, pos, (dir - 1) % 4, path + (pos,), True))
        
        if graph[pos][dir] is None: continue

        # Options for moving along to another corner
        if dir == WEST or dir == EAST:
            newPos = (graph[pos][dir], pos[1])
            newScore = score + abs(graph[pos][dir] - pos[0])
        elif dir == NORTH or dir == SOUTH:
            newPos = (pos[0], graph[pos][dir])
            newScore = score + abs(graph[pos][dir] - pos[1])

        newPath = path + (newPos, )
        heapq.heappush(queue, (newScore, newPos, dir, newPath, False))

    # Analyse final paths to get final path count
    pathPositions = set()
    for path in paths:
        minX, maxX = (path[0][0], path[1][0]) if path[0][0] <= path[1][0] else (path[1][0], path[0][0])
        minY, maxY = (path[0][1], path[1][1]) if path[0][1] <= path[1][1] else (path[1][1], path[0][1])
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                pathPositions.add((x, y))
    return len(pathPositions)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")