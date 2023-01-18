import copy

cubes = set()
minX = maxX = minY = maxY = minZ = maxZ = 0

maxValues = [0, 0, 0]
minValues = [0, 0, 0]

with open("input.txt") as file:
    for line in file.readlines():
        coords = tuple(int(i) for i in line[:-1].split(","))
        cubes.add(coords)
        for i, c in enumerate(coords):
            if c < minValues[i]: minValues[i] = c
            if c > maxValues[i]: maxValues[i] = c

outside = [(minX - 1, minY - 1, minZ - 1)]
outsideSet = set()

answer = 0
while len(outside):
    current = outside.pop(0)
    if current in outsideSet: continue
    outsideSet.add(current)
    for i in range(0, 3):
        for j in range(-1, 2, 2):
            newCoords = list(copy.copy(current))
            newCoords[i] += j
            newCoords = tuple(newCoords)

            if any(newCoords[k] > maxValues[k] + 1 for k in range(0, 3)): continue
            if any(newCoords[k] < minValues[k] - 1 for k in range(0, 3)): continue

            if newCoords in cubes: 
                answer += 1
                continue
            if newCoords in outsideSet: continue
            outside.append(newCoords)

print(f"The answer is {answer}")