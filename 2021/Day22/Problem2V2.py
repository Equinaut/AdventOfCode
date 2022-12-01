instructions = []
with open("inputSmall.txt", "r") as file:
    for line in file.readlines():
        instruction, coordsPart = line.split(" ")
        coords = coordsPart.split(",")
        coords = [[int(i) for i in part.split("=")[1].split("..")]
                  for part in coords]
        if instruction == "on": instructions.append((instruction, coords))

def intersect(bounds1, bounds2):
    ranges = [range(i[0], i[1]+1) for i in bounds1]

    for i, bound in enumerate(bounds2):
        if bound[0] not in ranges[i] and bound[1] not in ranges[i]: return False
    return True

instructions2 = []

for instruction, bounds in instructions:
    if all([not intersect(bounds, bounds2) for i, bounds2 in instructions2]): 
        instructions2.append((instruction, bounds))

for instruction in instructions2:
    if instruction in instructions: instructions.remove(instruction)

xBreakPoints, yBreakPoints, zBreakPoints = set(), set(), set()
breakPoints = [xBreakPoints, yBreakPoints, zBreakPoints]

for instruction, bounds in instructions2:
    for i, axisBounds in enumerate(bounds):
        breakPoints[i].add(axisBounds[0])
        breakPoints[i].add(axisBounds[1])             

for i, axisBreakPoints in enumerate(breakPoints):
    breakPoints[i] = list(breakPoints[i])
    breakPoints[i].sort()

print(breakPoints[0])
print(breakPoints[1])
print(breakPoints[2])

print()
print(instructions[0], instructions2[0])
print(len(instructions), len(instructions2))