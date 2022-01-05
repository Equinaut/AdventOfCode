instructions = []
with open("inputSmall.txt", "r") as file:
    for line in file.readlines():
        instruction, coordsPart = line.split(" ")
        coords = coordsPart.split(",")
        coords = [[int(i) for i in part.split("=")[1].split("..")]
                  for part in coords]
        instructions.append((instruction, coords))

def intersect(bounds1, bounds2):
    ranges = [range(i[0], i[1]+1) for i in bounds1]

    for i, bound in enumerate(bounds2):
        if bound[0] not in ranges[i] and bound[1] not in ranges[i]: return False
    return True

noIntersections = []
noIntersections.append(instructions.pop(0))


while len(instructions) > 0:
    currentInstruction = instructions.pop(0)
    print(len(instructions))

    intersects = False
    for instruction, bounds in noIntersections:

        if intersect(currentInstruction[1], bounds):
            intersects = True
            
            xBreaks = [currentInstruction[1][0][0]-1, currentInstruction[1][0][1]]
            yBreaks = [currentInstruction[1][1][0]-1, currentInstruction[1][1][1]]
            zBreaks = [currentInstruction[1][2][0]-1, currentInstruction[1][2][1]]

            if bounds[0][0] > xBreaks[0] and bounds[0][0] < xBreaks[1]: xBreaks.append(bounds[0][0])
            if bounds[0][1] > xBreaks[0] and bounds[0][1] < xBreaks[1]: xBreaks.append(bounds[0][1])
            if bounds[1][0] > yBreaks[0] and bounds[1][0] < yBreaks[1]: yBreaks.append(bounds[1][0])
            if bounds[1][1] > yBreaks[0] and bounds[1][1] < yBreaks[1]: yBreaks.append(bounds[1][1])
            if bounds[2][0] > zBreaks[0] and bounds[2][0] < zBreaks[1]: zBreaks.append(bounds[2][0])
            if bounds[2][1] > zBreaks[0] and bounds[2][1] < zBreaks[1]: zBreaks.append(bounds[2][1])
            xBreaks.sort()
            yBreaks.sort()
            zBreaks.sort()


            newInstructions = []
            
            for a, xStart in enumerate(xBreaks[:-1]):
                xEnd = xBreaks[a+1]
                for b, yStart in enumerate(yBreaks[:-1]):
                    yEnd = yBreaks[b+1]
                    for c, zStart in enumerate(zBreaks[:-1]):
                        zEnd = zBreaks[c+1]
                        newInstructions.append((currentInstruction[0], [[xStart + 1, xEnd], [yStart + 1, yEnd], [zStart + 1, zEnd]]))

            for newInstruction in newInstructions:
                instructions.insert(0, newInstruction)
            break

    if not intersects: noIntersections.append(currentInstruction)