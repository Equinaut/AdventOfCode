fish = dict()

for i in range(-1, 9): fish[i] = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        for i in line.split(","):
            fish[int(i)] += 1

def genNewGeneration(fish):
    newFish = dict()
    keys = list(fish.keys())
    newAmount = 0
    for key in keys:
        amount = fish[key]
        if key != 0:
            newFish[key - 1] = amount
        else:
            newAmount = amount
        fish[key] = 0

    if newAmount > 0:
        if 6 in newFish: newFish[6] += newAmount
        else: newFish[6] = newAmount
        if 8 in newFish: newFish[8] += newAmount
        else: newFish[8] = newAmount
        
    for key, amount in newFish.items(): fish[key] = amount


for i in range(0, 256): genNewGeneration(fish)

print(f"The answer is {sum(list(fish.values()))}")