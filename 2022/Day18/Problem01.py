cubes = set()
with open("input.txt") as file:
    cubes = {tuple([int(i) for i in line[:-1].split(",")]) for line in file.readlines()}

answer = 0
for cube in cubes:
    for i in range(0, 3):
        for j in range(-1, 2, 2):
            newCoords = [0, 0, 0]
            newCoords[i] = j
            newCoords = (cube[0] + newCoords[0], cube[1] + newCoords[1], cube[2] + newCoords[2])
            if (newCoords in cubes): answer += 1

print(f"The answer is {len(cubes) * 6 - answer}")