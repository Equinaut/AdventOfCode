with open("input.txt") as file:
    wind = file.readlines()[0]
windIndex = 0

filledAreas = set()
topY = 0

for x in range(0, 8): filledAreas.add((x, -1))

def createNewRock(rockNumber):
    if rockNumber == 0: 
        return {
            (2, topY + 3), 
            (3, topY + 3), 
            (4, topY + 3), 
            (5, topY + 3)
        }
    if rockNumber == 1: 
        return {
            (2, topY + 4), 
            (3, topY + 4), 
            (4, topY + 4), 
            (3, topY + 3), 
            (3, topY + 5)
        }
    if rockNumber == 2:
        return {
            (2, topY + 3),
            (3, topY + 3),
            (4, topY + 3),
            (4, topY + 4),
            (4, topY + 5)
        }
    if rockNumber == 3:
        return {
            (2, topY + 3),
            (2, topY + 4),
            (2, topY + 5),
            (2, topY + 6)
        }
    if rockNumber == 4:
        return {
            (2, topY + 4),
            (3, topY + 4),
            (2, topY + 3),
            (3, topY + 3)
        }

def rowEmpty(row):
    for x in range(0, 7):
        if (x, row) in filledAreas: return False
    return True

def collision(rock):
    for (x, y) in rock:
        if x < 0 or x >= 7: return True
        if (x, y) in filledAreas: return True
    return False

def moveSide(rock, amount):
    newRock = {(x+amount, y) for (x, y) in rock}
    if collision(newRock): return None
    return newRock

def moveDown(rock):
    newRock = {(x, y-1) for (x, y) in rock}
    if collision(newRock): return None
    return newRock

def addRock(rock):
    global windIndex
    global topY
    while True:

        direction = wind[windIndex]
        windIndex = (windIndex + 1) % len(wind)
        if direction == ">":
            newRock = moveSide(rock, 1)
        elif direction == "<":
            newRock = moveSide(rock, -1)
        
        if newRock is not None: rock = newRock
        
        
        newRock = moveDown(rock)
        if newRock == None: break
        rock = newRock

    for (x, y) in rock:
        filledAreas.add((x, y))
    
    while not rowEmpty(topY): topY += 1

def printState(rock = None):
    for y in range(20, -1, -1):
        for x in range(0, 7):
            if (x, y) in filledAreas: print("#", end="")
            elif rock is not None and (x, y) in rock: print("@", end="")                
            else: print(".", end="")
        print()

for i in range(0, 2022):
    addRock(createNewRock(i % 5))

answer = 0
print(f"The answer is {topY}")