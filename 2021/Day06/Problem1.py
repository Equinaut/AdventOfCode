fish = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        fish.extend([int(i) for i in line.split(",")])

def genNewGeneration():
    for i, age in enumerate(fish):
        fish[i] -= 1
        
        if fish[i] == -1: 
            fish[i] =6
            fish.append(9)

for i in range(0, 80): genNewGeneration()

print(f"The answer is {len(fish)}")