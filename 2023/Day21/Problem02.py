import functools
import numpy as np

COMPLETE_LEVEL = 500
TOTAL_MOVES = 26501365

def main():
    positions = set()
    with open("input.txt") as file:
        for y, line in enumerate(file):
            for x, c in enumerate(line[:-1]):
                if c == ".":
                    positions.add((x, y))
                elif c == "S": 
                    start = (x, y)
                    positions.add((x, y))
        height = y + 1
        width = x + 1

    a = solveForMoves(positions, width, height, 65, start)
    b = solveForMoves(positions, width, height, 65 + 131, start)
    c = solveForMoves(positions, width, height, 65 + 131 + 131, start)

    coefficients = np.polyfit((1,2,3), (a,b,c),2)
    val = (TOTAL_MOVES - 65) // 131 + 1
    return int(coefficients[0]) * val ** 2 + int(coefficients[1]) * val + int(coefficients[2])

def solveForMoves(positions, width, height, movesIn, start):
    GRIDSX = 1 + movesIn // width
    GRIDSY = 1 + movesIn // height
    ans = 0

    for x in range(-GRIDSX, GRIDSX + 1):
        y = -GRIDSY + x
        upperBound = GRIDSY + 1 - x

        if y < 0:
            minY = -GRIDSY + x
            maxY = 0
            while minY + 1 < maxY:
                mid = (minY + maxY) // 2
                moves = movesIn - distToGrid((width, height), start, x, mid)
                if moves < 0: minY = mid
                else: maxY = mid
            y = mid - 1
            upperBound = min(upperBound, abs(mid) + 5)
            
        while movesIn - distToGrid((width, height), start, x, y) < 0 and y < 0:
            y += 1

        while y < upperBound:
            moves = movesIn - distToGrid((width, height), start, x, y)

            if moves < 0: 
                y += 1
                continue

            if moves < 0 and y > 0: 
                break
            startPos = otherGridStart(start, (width, height), x, y)
            if moves > COMPLETE_LEVEL:
                moves = COMPLETE_LEVEL + ((moves - COMPLETE_LEVEL) % 2)
                if y < 0:
                    evenCount = (abs(y) // 2)
                    oddCount = (abs(y + 1) // 2)
                    ans += singleMapReachable(positions, startPos, COMPLETE_LEVEL) * evenCount
                    ans += singleMapReachable(positions, startPos, COMPLETE_LEVEL + 1) * oddCount
                    y = 0
                    break
            
            ans += singleMapReachable(positions, startPos, moves)
            y += 1
    return ans

def expandGrid(positions, width, height):
    newPositions = set()
    for p in positions:
        newPositions.add(p)
        newPositions.add((p[0] + width, p[1]))
    return newPositions

singleMapReachableCache = dict()
def singleMapReachable(positions, start, moves):
    if moves > COMPLETE_LEVEL: moves = COMPLETE_LEVEL + ((moves - COMPLETE_LEVEL) % 2)

    if (start, moves) in singleMapReachableCache: 
        return singleMapReachableCache[start, moves]
    
    reachablePositions = set()
    reachablePositions.add(start)

    for i in range(moves):
        newReachablePositions = set()
        for pos in reachablePositions:
            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newNode = (pos[0] + offset[0], pos[1] + offset[1])
                if newNode not in positions: continue
                newReachablePositions.add(newNode)
        reachablePositions = newReachablePositions

    singleMapReachableCache[start, moves] = len(reachablePositions)
    return len(reachablePositions)


@functools.cache
def distToGrid(size, start, gridX, gridY):
    ans = 0
    width, height = size
    if gridX > 1: 
        ans += width * (gridX - 1)
        gridX = 1
    elif gridX < -1:
        ans += width * (-1 - gridX)
        gridX = -1
    if gridY > 1: 
        ans += height * (gridY - 1)
        gridY = 1
    elif gridY < -1:
        ans += height * (-1 - gridY)
        gridY = -1
    if abs(gridX) == 1: ans += width // 2 + 1
    if abs(gridY) == 1: ans += height // 2 + 1
    return ans

def otherGridStart(start, size, gridX, gridY):
    width, height = size
    if gridX == 0: x = start[0]
    elif gridX < 0: x = width - 1
    elif gridX > 0: x = 0

    if gridY == 0: y = start[1]
    elif gridY < 0: y = height - 1
    elif gridY > 0: y = 0
    return x, y

if __name__ == "__main__":
    print(f"The answer is {main()}")