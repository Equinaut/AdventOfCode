from enum import Enum

def getArea(p1, p2): return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

class SquareType(Enum):
    Outside = 0
    Edge = 1
    Inside = 2

def main():
    points = []
    xCoords, yCoords = set(), set()
    with open("input.txt") as file:
        for line in file:
            x, y = tuple(map(int, line[:-1].split(",")))
            points.append((x, y))
            for i in range(-1, 2):
                xCoords.add(x + i)
                yCoords.add(y + i)
    
    # Get sorted list of X and Y coordinates
    xCoords = list(sorted(xCoords))
    yCoords = list(sorted(yCoords))
    # Use sorted list of X and Y coordinates to reduce shape down to smaller grid
    reducedPoints = [(xCoords.index(x), yCoords.index(y)) for (x, y) in points]
    xMax, yMax = len(xCoords), len(yCoords)

    # What type of cell each cell in the grid is
    # Either Inside, Edge or Outside
    # Initially everything is set to Inside
    shapeValues = [[SquareType.Inside] * (xMax + 1) for _ in range(yMax + 2)]
    
    # Add first point to end of points list to complete the loop
    reducedPoints.append(reducedPoints[0])

    # Then the edges are marked as Edges
    for i in range(0, len(reducedPoints) - 1):
        p1, p2 = reducedPoints[i], reducedPoints[i + 1]
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                shapeValues[y][x] = SquareType.Edge

    # Then use flood fill from the top left, to mark all of the outside cells as outside
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if x < 0 or x > xMax or y < 0 or y > yMax + 1: continue
        if shapeValues[y][x] != SquareType.Inside: continue
        shapeValues[y][x] = SquareType.Outside
        stack.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

    # Scan down each column in the grid, and record for each position in the shape, the y coordinate where the shape started
    startedGrid = [[-1] * (xMax + 1) for _ in range(yMax + 2)]
    for x in range(0, xMax + 1):
        started = -1
        for y in range(0, yMax + 2):
            if shapeValues[y][x] == SquareType.Outside: started = -1 # End of shape
            elif started == -1: started = y # Start of shape
            startedGrid[y][x] = started

    # Get sorted list of possible rectangles in descending order
    rectangles = []
    for i, (x1, y1) in enumerate(reducedPoints[:-1]):
        for j, (x2, y2) in enumerate(reducedPoints[:i]):
            rectangles.append((getArea(points[i], points[j]), (i, j), (x1, y1, x2, y2)))
    rectangles.sort(reverse=True)

    # Check rectangles in order of size, until a valid one is found, the first valid one is the solution
    for (area, (i, j), (x1, y1, x2, y2)) in rectangles:
        minX, maxX = min(x1, x2), max(x1, x2)
        minY, maxY = min(y1, y2), max(y1, y2)
        for x in range(minX, maxX + 1):
            if startedGrid[maxY][x] == -1 or startedGrid[maxY][x] > minY: break
        else: return area

if __name__ == "__main__":
    print(f"The answer is {main()}")
