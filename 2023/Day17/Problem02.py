LEFT = 1
UP = 2
RIGHT = 3
DOWN = 4

def main():
    ans = 0
    with open("input.txt") as file:
        positions = dict()
        for y, line in enumerate(file):
            for x, c in enumerate(line[:-1]):
                positions[x,y] = int(c)
                final_pos = (x, y)

        distances = dict()
        prevNodes = dict()
        distances[0, 0, RIGHT] = 0
        distances[0, 0, DOWN] = 0
        prevNodes[0, 0, RIGHT] = None
        prevNodes[0, 0, DOWN] = None
        visited = set()
        nextNodes = set()

        currentNode = (0, 0, RIGHT)
        nextNodes = set()

        while currentNode[:2] != final_pos:
            prevDirection = currentNode[2]

            for distTemp in range(3, 11):
                for dirTemp in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    xOff = dirTemp[0] * distTemp
                    yOff = dirTemp[1] * distTemp
                    if xOff == 0 and yOff == 0: continue

                    try:
                        newDirection = getPrevDirection((0, 0), (xOff, yOff))
                    except ValueError: 
                        continue
                    
                    if tooLong((0, 0), (xOff, yOff)): continue
                    if xOff != 0 and yOff != 0: continue
                    newPos = (currentNode[0] + xOff, currentNode[1] + yOff, newDirection)
                    
                    if newPos == currentNode: continue
                    if newPos[:2] not in positions: continue
                    if newPos in visited: continue

                    distanceIncrease = 0
                    a = []
                    for xTemp in range(1, xOff + 1): 
                        distanceIncrease += positions[currentNode[0] + xTemp, currentNode[1]]
                        a.append((positions[currentNode[0] + xTemp, currentNode[1]]))
                    for xTemp in range(-1, xOff - 1, -1): 
                        distanceIncrease += positions[currentNode[0] + xTemp, currentNode[1]]
                        a.append((positions[currentNode[0] + xTemp, currentNode[1]]))
                    for yTemp in range(1, yOff + 1): 
                        distanceIncrease += positions[currentNode[0], currentNode[1] + yTemp]
                        a.append((positions[currentNode[0], currentNode[1] + yTemp]))
                    for yTemp in range(-1, yOff - 1, -1): 
                        distanceIncrease += positions[currentNode[0], currentNode[1] + yTemp]
                        a.append((positions[currentNode[0], currentNode[1] + yTemp]))

                    if tooLong(newPos, prevNodes[currentNode]): continue
                    if prevDirection == newDirection: continue
                    newDist = distances[currentNode] + distanceIncrease
                    nextNodes.add(newPos)
                    if newPos not in distances or newDist < distances[newPos]: 
                        nextNodes.add(newPos)
                        distances[newPos] = newDist
                        prevNodes[newPos] = currentNode

            visited.add(currentNode)

            try:
                currentNode = min(nextNodes, key = lambda a: distances[a])
                nextNodes.remove(currentNode)
            except ValueError:
                break

    target = final_pos
    endDir = min(range(1, 5), key = lambda d: float("inf") if (*target, d) not in distances else distances[target[0], target[1], d])
    ans = distances[target[0], target[1], endDir]
    path = set()
    currentNode = (*target, endDir)
    while currentNode is not None:
        path.add(currentNode)
        currentNode = prevNodes[currentNode]
    return ans

def tooLong(pos1, pos2):
    if pos2 is None: return False
    xDiff = abs(pos1[0] - pos2[0])
    yDiff = abs(pos1[1] - pos2[1])
    if xDiff < 4 and yDiff < 4: return True
    if xDiff > 10: return True
    if yDiff > 10: return True
    return False

def getPrevDirection(prevNode, node):
    if prevNode is None: return None
    xDist, yDist = 0,0
    if node[0] > prevNode[0]: xDist = 1
    if node[0] < prevNode[0]: xDist = 1
    if node[1] > prevNode[1]: yDist = 1
    if node[1] < prevNode[1]: yDist = 1

    if (xDist, yDist) == (1, 0): return RIGHT
    if (xDist, yDist) == (-1, 0): return LEFT
    if (xDist, yDist) == (0, 1): return DOWN
    if (xDist, yDist) == (0, -1): return UP
    raise ValueError(f"Invalid direction from {prevNode} to {node}")

if __name__ == "__main__":
    print(f"The answer is {main()}")