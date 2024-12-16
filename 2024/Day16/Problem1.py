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
        graph = dict()
        start = end = None
        minDist = dict()
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

    queue = [(0, start, EAST)]
    while queue:
        score, pos, dir = heapq.heappop(queue)
        if minDist[pos][dir] is not None and score >= minDist[pos][dir]: continue
        else: minDist[pos][dir] = score

        if pos == end: return score

        # Options for turning the corner
        heapq.heappush(queue, (score + 1000, pos, (dir + 1) % 4))
        heapq.heappush(queue, (score + 1000, pos, (dir - 1) % 4))
        
        if graph[pos][dir] is None: continue

        # Options for moving along to another corner
        if dir == WEST or dir == EAST:
            heapq.heappush(queue, (score + abs(graph[pos][dir] - pos[0]), (graph[pos][dir], pos[1]), dir))
        elif dir == NORTH or dir == SOUTH:
            heapq.heappush(queue, (score + abs(graph[pos][dir] - pos[1]), (pos[0], graph[pos][dir]), dir))

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")