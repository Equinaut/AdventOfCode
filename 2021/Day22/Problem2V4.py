instructions = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        instruction, coordsPart = line.split(" ")
        coords = coordsPart.split(",")
        coords = [[int(i) for i in part.split("=")[1].split("..")]
                  for part in coords]
        instructions.append((instruction, coords))

for i in range(0, len(instructions)):
    for j in range(0, 3):
        instructions[i][1][j][1]+=1

zBreaks = set()

for instruction, bounds in instructions:
    zBreaks.add(bounds[2][0])
    zBreaks.add(bounds[2][1])
zBreaks = list(zBreaks)
zBreaks.sort()

answer = 0

for zIndex, z in enumerate(zBreaks[:-1]):

    zWidth = abs(zBreaks[zIndex+1] - z)

    reducedInstructions = []

    for instruction in instructions:
        if z >= instruction[1][2][0] and z < instruction[1][2][1]:
            reducedInstructions.append(
                (
                    instruction[0], 
                    [[instruction[1][0][0], instruction[1][0][1]], [instruction[1][1][0], instruction[1][1][1]]]
                )
            )
    
    yBreaks = set()

    for instruction2, bounds2 in reducedInstructions:
        yBreaks.add(bounds2[1][0])
        yBreaks.add(bounds2[1][1])
    yBreaks = list(yBreaks)
    yBreaks.sort()

    for yIndex, y in enumerate(yBreaks[:-1]):

        yWidth = abs(y - yBreaks[yIndex+1])

        reducedInstructions2 = []
        for instruction2, bounds2 in reducedInstructions:
            if y >= bounds2[1][0] and y < bounds2[1][1]:
                reducedInstructions2.append(
                    (
                        instruction2,
                        [bounds2[0][0], bounds2[0][1]]
                    )
                )

        xBreaks = set()
        for instruction3, bounds3 in reducedInstructions2:
            xBreaks.add(bounds3[0])
            xBreaks.add(bounds3[1])
        xBreaks = list(xBreaks)
        xBreaks.sort()

        for xIndex, x in enumerate(xBreaks[:-1]):
            
            xWidth = abs(x - xBreaks[xIndex+1])

            reducedInstructions3 = []
            for (instruction3, bounds3) in reducedInstructions2:
                if x >= bounds3[0] and x < bounds3[1]:
                    reducedInstructions3.append(instruction3)
                    

            if len(reducedInstructions3) > 0 and reducedInstructions3[-1] == "on": 

                answer += zWidth * yWidth * xWidth

print(f"The answer is {answer}")