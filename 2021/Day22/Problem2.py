instructions = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        instruction, coordsPart = line.split(" ")
        coords = coordsPart.split(",")
        coords = [[int(i) for i in part.split("=")[1].split("..")] for part in coords]
        instructions.append((instruction, coords))

allXBreaks = allYBreaks = allZBreaks = set()

for instruction, ((xMin, xMax), (yMin, yMax), (zMin, zMax)) in instructions:
    allXBreaks.add(xMin)
    allXBreaks.add(xMax)
    allYBreaks.add(yMin)
    allYBreaks.add(yMax)
    allZBreaks.add(zMin)
    allZBreaks.add(zMax)

allXBreaks = list(allXBreaks)
allYBreaks = list(allYBreaks)
allZBreaks = list(allZBreaks)

allXBreaks.sort()
allYBreaks.sort()
allZBreaks.sort()

newInstructions = []


for instruction, breakPoints in instructions:
    theseBreaks = []
    for breakPoint in allXBreaks:
        if breakPoint > breakPoints[0][1]: break
        if breakPoint >= breakPoints[0][0]:
            theseBreaks.append(breakPoint)
    for i, startPoint in enumerate(theseBreaks[:-1]):
        endPoint = theseBreaks[i+1]
        newInstructions.append([
            instruction,
            [[startPoint, endPoint], [breakPoints[1][0], breakPoints[1][1]], [breakPoints[2][0], breakPoints[2][1]]]
        ])
instructions = newInstructions
newInstructions = []

print("Xdone")

for j,(instruction, breakPoints) in enumerate(instructions):
    theseBreaks = []
    if j%100==0: print(j / len(instructions), len(newInstructions))


    for breakPoint in allYBreaks:
        if breakPoint > breakPoints[1][1]: break
        if breakPoint >= breakPoints[1][0]:
            theseBreaks.append(breakPoint)
    for i, startPoint in enumerate(theseBreaks[:-1]):
        endPoint = theseBreaks[i+1]
        newInstructions.append([
            instruction,
            [[breakPoints[0][0], breakPoints[0][1]], [startPoint, endPoint], [breakPoints[2][0], breakPoints[2][1]]]
        ])
instructions = newInstructions
newInstructions = []

print("Ydone")
for j, (instruction, breakPoints) in enumerate(instructions):
    theseBreaks = []
    if j % 100 == 0:
        print(j / len(instructions), len(newInstructions))

    
    for breakPoint in allZBreaks:
        if breakPoint > breakPoints[2][1]: break
        if breakPoint >= breakPoints[2][0]:
            theseBreaks.append(breakPoint)
    for i, startPoint in enumerate(theseBreaks[:-1]):
        endPoint = theseBreaks[i+1]
        newInstructions.append([
            instruction,
            [[breakPoints[0][0], breakPoints[0][1]], [breakPoints[1][0], breakPoints[1][1]], [startPoint, endPoint]]
        ])
instructions = newInstructions

print("Zdone")

print(len(instructions))
