directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def getSideCount(region):
    # Checks each square in the region to see if it is an edge piece in each direction, also tests an adjacent piece
    # If an adjacent piece is found that also qualifies as an edge, then this edge can be ignored, this makes sure
    # That only one edge is counted  from each side
    ans = 0
    for pos in region[1]:
        for d in directions:
            nextPosition = (pos[0] + d[0], pos[1] + d[1])
            adjacentPosition = (pos[0] + d[1], pos[1] + d[0])
            adjecentNextPosition = (pos[0] + d[0] + d[1], pos[1] + d[0] + d[1])
            if (nextPosition not in region[1]) and not (adjacentPosition in region[1] and adjecentNextPosition not in region[1]): ans += 1
    return ans

def getArea(region):
    return len(region[1])

def main():
    with open("input.txt") as file:
        grid = [list(line[:-1]) for line in file.readlines()]
    
    regions = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            if grid[y][x] == None: continue
            regions.append((grid[y][x], set()))
            queue = [(x, y)]
            
            while queue:
                pos = queue.pop()
                regions[-1][1].add(pos)
                grid[pos[1]][pos[0]] = None
                for d in directions:
                    nextPos = (pos[0] + d[0], pos[1] + d[1])
                    if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(grid[0]) or nextPos[1] >= len(grid): continue
                    if grid[nextPos[1]][nextPos[0]] == regions[-1][0]:
                        queue.append(nextPos)

    return sum(getSideCount(r) * getArea(r) for r in regions)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")