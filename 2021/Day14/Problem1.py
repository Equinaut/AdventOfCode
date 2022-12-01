currentString = []
pairs = {}

with open("input.txt", "r") as file:
    currentString = file.readline()[:-1]
    file.readline()
    for line in file.readlines():
        pairs[line.split(" -> ")[0]] = line[:-1].split(" -> ")[1]

for iteration in range(10):
    i = 1
    while i < len(currentString):
        currentString = currentString[:i] + pairs[currentString[i-1:i+1]] + currentString[i:]
        i+=2

letterCounts = {l: currentString.count(l) for l in currentString}

print(f"The answer is {max(letterCounts.values()) - min(letterCounts.values())}")