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

    underBricks = dict()
    for x,y,z in brickPositions2:
        b = brickPositions2[x,y,z]
        if b not in underBricks:
            underBricks[b] = set()
        if (x,y,(z - 1)) in brickPositions2:
            if brickPositions2[x,y,z-1] == b: continue
            underBricks[b].add(brickPositions2[x,y,z-1])

    supports = dict()
    for b in allBricks: supports[b] = set()

    for b in underBricks:
        for c in underBricks[b]:
            supports[c].add(b)
    
    canRemove = set()
    for b in supports:
        if len(supports[b]) == 0: canRemove.add(b)
        if all(len(underBricks[c]) > 1 for c in supports[b]): canRemove.add(b)

    return len(canRemove)

if __name__ == "__main__":
    print(f"The answer is {main()}")