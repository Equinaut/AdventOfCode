instructions = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        instruction, coordsPart = line.split(" ")
        coords = coordsPart.split(",")
        coords = [[int(i) for i in part.split("=")[1].split("..")] for part in coords]
        instructions.append((instruction, coords))


grid = set()

for instruction, (xPart, yPart, zPart) in instructions:
    for x in range(max(-50, xPart[0]), min(51, xPart[1] + 1)):
        for y in range(max(-50, yPart[0]), min(51, yPart[1] + 1)):
            for z in range(max(-50, zPart[0]), min(51, zPart[1] + 1)):
                if instruction=="on": grid.add((x, y, z))
                elif (x, y, z) in grid: grid.remove((x,y,z))

print(f"The answer is {len(grid)}")