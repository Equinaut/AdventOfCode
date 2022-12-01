grid = []
instructions = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line != "\n": 
        x, y = [int(i) for i in line[:-1].split(",")]
        grid.append((x, y))
        line = file.readline()
    
    for line in file.readlines():
        instruction = line[:-1].split(" ")[-1]
        instructions.append((instruction[0], int(instruction.split("=")[-1])))

instruction = instructions[0]
if instruction[0] == "y":
    yCoord = instruction[1]
    for i, item in enumerate(grid):
        x, y = item
        if y > yCoord:
            grid[i] = (x, yCoord - (y - yCoord))

    grid = list(set(grid))
else:
    xCoord = instruction[1]
    for i, item in enumerate(grid):
        x, y = item
        if x > xCoord:
            grid[i] = (xCoord - (x - xCoord), y)

    grid = list(set(grid))

print(f"The answer is {len(grid)}")