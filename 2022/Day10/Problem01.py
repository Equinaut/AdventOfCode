cycle = X = 1
xAtCycle = dict()

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

answer = sum(xAtCycle[i] * i for i in range(20,221,40))

print(f"The answer is {answer}")