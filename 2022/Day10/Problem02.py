cycle = X = 1
xAtCycle = {1 : X}

with open("input.txt") as file:
    for line in file.readlines():
        if line.startswith("noop"):
            cycle += 1
            xAtCycle[cycle] = X
        elif line.startswith("addx"):
            v = int(line[:-1].split(" ")[1])
            cycle += 1
            xAtCycle[cycle] = X
            cycle += 1
            X += v
            xAtCycle[cycle] = X

for row in range(0, 6):
    currentRow = ""
    for i in range(0, 40): 
        cycle = row * 40 + i + 1
        currentRow = currentRow + ("#" if (xAtCycle[cycle] == i) or (xAtCycle[cycle] == i + 1) or (xAtCycle[cycle] == i - 1) else " ")

    print("".join(currentRow))
