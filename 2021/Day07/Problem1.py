numbers = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        for i in line.split(","): numbers.append(int(i))

minFuel = sum(numbers)

for i in range(min(numbers), max(numbers)):
    newMinFuel = sum([abs(i - value) for j, value in enumerate(numbers)])
    if newMinFuel < minFuel:
        minFuel = newMinFuel

print(f"The answer is {minFuel}")
