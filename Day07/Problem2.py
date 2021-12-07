numbers = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        for i in line.split(","): numbers.append(int(i))

minFuel = None

for i in range(min(numbers), max(numbers)):
    newMinFuel = sum([(abs(value - i) + 1) * abs(value - i) / 2 for j, value in enumerate(numbers)])
    if minFuel is None or newMinFuel < minFuel:
        minFuel = newMinFuel

print(f"The answer is {int(minFuel)}")
