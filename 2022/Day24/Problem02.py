from math import lcm

with open("input.txt") as file:
    text = file.readlines()
    height, width = len(text) - 2, len(text[0]) - 3

    currentPosition = (1, 0)
    blizzards = set()
    for y in range(1, len(text)):
        for x in range(1, len(text[y])):
            if text[y][x] in "<>^v":
                blizzards.add((text[y][x], x, y))
    
def nextBlizzardState(blizzards):
    newBlizzards = set()
    for direction, x, y in blizzards:
        if direction == ">":
            newX = x + 1
            newY = y
            if newX > width: newX = 1
        elif direction == "<":
            newX = x - 1
            newY = y
            if newX <= 0: newX = width
        elif direction == "v":
            newX = x 
            newY = y + 1
            if newY > height: newY = 1
        elif direction == "^":
            newX = x
            newY = y - 1
            if newY <= 0: newY = height
        
        newBlizzards.add((direction, newX, newY))
    return newBlizzards

def genNextStates(state, start, goal):
    (currentX, currentY), time = state
    newStates = []
    for (newX, newY) in [(currentX + 1, currentY), (currentX, currentY + 1), (currentX, currentY), (currentX - 1, currentY), (currentX, currentY - 1)]:
        if (newX, newY) == goal: return [((newX, newY), time + 1)]

        if (newX <= 0 or newX > width or newY <= 0 or newY >= height + 1) and ((newX, newY) != start): continue

        newBlizzards = blizzardStates[(time + 1) % (lcm(width, height))]

        if any((direction, newX, newY) in newBlizzards for direction in "<>^v"): continue

        newStates.append(((newX, newY), time + 1))
    return newStates

blizzardStates = [blizzards]
while len(blizzardStates) < lcm(width, height):
    blizzardStates.append(nextBlizzardState(blizzardStates[-1]))

stateKey = lambda state: (state[0], state[1] % width * height)

def shortestTime(startState, goal):
    doneStates = set()
    minSoFar = None
    states = [startState]
    while states:
        state = states.pop(0)
        (x, y), time = state
        if stateKey(state) in doneStates: continue
        if minSoFar and time > minSoFar: continue

        doneStates.add(stateKey(state))
        
        if (x, y) == goal:
            if minSoFar is None or state[1] < minSoFar: 
                minSoFar = time

        states.extend(genNextStates(state, startState[0], goal))
    return minSoFar


firstTrip = shortestTime(((1, 0), 0), (width, height + 1))
secondTrip = shortestTime(((width, height + 1), firstTrip), (1, 0))
finalTrip = shortestTime(((1, 0), secondTrip), (width, height + 1))

print(f"The answer is {finalTrip}")