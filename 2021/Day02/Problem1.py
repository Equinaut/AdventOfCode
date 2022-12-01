totalForward = 0
totalDepth = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        if line.split(" ")[0] == "forward": totalForward += int(line.split(" ")[1])
        if line.split(" ")[0] == "down": totalDepth += int(line.split(" ")[1])
        if line.split(" ")[0] == "up": totalDepth -= int(line.split(" ")[1])

print(f"The answer is {totalForward * totalDepth}")
        