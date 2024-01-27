import copy

def main():
    brickPositions = dict()
    brickPositions2 = dict()
    allBricks = set()
    with open("input.txt") as file:
        for brickNumber, line in enumerate(file):
            b = brickNumber
            allBricks.add(b)
            brickPositions[b] = set()
            x1,y1,z1,x2,y2,z2 = line[:-1].replace("~",",").split(",")
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    for z in range(int(z1), int(z2) + 1):
                        brickPositions[b].add((x, y, z))
                        brickPositions2[x, y, z] = b
    
    # Move bricks down
    lastMovedOne = True
    i = 0
    while lastMovedOne:
        i += 1
        lastMovedOne = False
        for b in brickPositions:
            newBrickPositions = {(x, y, z - 1) for (x, y, z) in brickPositions[b]}
            if min([z for (_,_,z) in newBrickPositions]) <= 0: continue
            if all(newPos not in brickPositions2 or brickPositions2[newPos] == b for newPos in newBrickPositions):
                for p in brickPositions[b]: del brickPositions2[p]
                for p in newBrickPositions: brickPositions2[p] = b 
                brickPositions[b] = newBrickPositions
                lastMovedOne = True

    return sum(map(lambda start: len(calculateChain(copy.deepcopy(brickPositions), copy.deepcopy(brickPositions2), start)), allBricks))

def calculateChain(brickPositions, brickPositions2, start):
    removed = []
    for p in brickPositions[start]:
        del brickPositions2[p]
    del brickPositions[start]

    removedOne = True
    while removedOne:
        toRemove = set()
        for brick in brickPositions:
            # Check if brick is currently supproted
            for (x, y, z) in brickPositions[brick]:
                if z <= 1: break
                if (x, y, z - 1) in brickPositions2 and brickPositions2[x,y,z - 1] != brick: break
            else: toRemove.add(brick) # if brick is not supported, add to toRemove queue

        for brick in toRemove:
            removed.append(brick)
            for p in brickPositions[brick]: del brickPositions2[p]
            del brickPositions[brick]
        removedOne = len(toRemove) > 0
    return removed

if __name__ == "__main__":
    print(f"The answer is {main()}")