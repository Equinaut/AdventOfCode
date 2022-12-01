aim = 0
horizontalPosition = 0
depth = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        instruction, value = line.split(" ")
        if instruction == "forward": 
            horizontalPosition += int(value)
            depth += int(value) * aim
        elif instruction == "up": aim -= int(value)
        elif instruction == "down": aim += int(value)

print(f"The answer is {horizontalPosition * depth}")