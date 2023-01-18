with open("input.txt") as file:
    wind = file.readlines()[0]
windIndex = 0

filledAreas = set()
topY = 0

for x in range(0, 8): filledAreas.add((x, -1))

def createNewRock(rockNumber):
    if rockNumber == 0: return {(i, topY + 3) for i in range(2, 6)}, topY + 4
    if rockNumber == 1: return {(i, topY + 4) for i in [2,3,4]} | {(3, topY + i) for i in [3, 5]}, topY + 6
    if rockNumber == 2: return {(i, topY + 3) for i in [2, 3]} | {(4, topY + i) for i in [3, 4, 5]}, topY + 6
    if rockNumber == 3: return {(2, topY + i) for i in range(3, 7)}, topY + 7
    if rockNumber == 4: return {(i, topY + j) for i in [2,3] for j in [3,4]}, topY + 5

def collision(rock):
    if rock.intersection(filledAreas): return True
    for (x, y) in rock:
        if x < 0 or x >= 7: return True
    return False

def moveSide(rock, amount):
    newRock = {(x + amount, y) for (x, y) in rock}
    if collision(newRock): return None
    return newRock

def moveDown(rock):
    newRock = {(x, y - 1) for (x, y) in rock}
    if collision(newRock): return None
    return newRock

def addRock(rock, maxY, filledAreas, topY, windIndex):
    while True:
        direction = wind[windIndex]
        windIndex = ((windIndex + 1) % len(wind))
        if direction == ">": newRock = moveSide(rock, 1)
        elif direction == "<": newRock = moveSide(rock, -1)
        if newRock is not None: rock = newRock

        newRock = moveDown(rock)
        if newRock == None: break
        maxY -= 1
        rock = newRock

    for (x, y) in rock: filledAreas.add((x, y))
    if maxY > topY: topY = maxY

    return topY, windIndex

def getTopRows(filledAreas):
    newFilledAreas = set()
    for x in range(0, 7):
        for y in range(topY - 20, topY):
            if (x, y) in filledAreas:
                newFilledAreas.add((x, y - topY))
    return newFilledAreas

convertTopRows = lambda filledAreas: "".join("1" if (x, y) in filledAreas else "0" for x in range(0, 7) for y in range(topY - 20, topY))

def doCycles(n):
    if n == 0: return
    global topY
    global windIndex
    global filledAreas

    startTopY = topY
    key = (n, windIndex, convertTopRows(filledAreas))
    if key in cache:
        windIndex, newFilledAreas, topYIncrease = cache[key]
        topY += topYIncrease

        filledAreas = set()
        for (x, y) in newFilledAreas:
            filledAreas.add((x, y + topY))
    else:
        if n >= 10:
            for _ in range(10): doCycles(n // 10)
            doCycles(n % 10) 
        else:
            for j in range(n * 5): topY, windIndex = addRock(*createNewRock(j % 5), filledAreas, topY, windIndex)
        cache[key] = (windIndex, getTopRows(filledAreas), topY - startTopY)

cache = dict()

maxI = (10 ** 12)
doCycles(maxI // 5)

print(f"The answer is {topY}")