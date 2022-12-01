currentString = []
pairs = {}

with open("input.txt", "r") as file:
    currentString = file.readline()[:-1]
    file.readline()
    for line in file.readlines():
        pairs[line.split(" -> ")[0]] = line[:-1].split(" -> ")[1]

def nextIteration(pairCounts):
    newPairCounts = {}
    for pair, count in pairCounts.items():
        newPair1 = pair[0]+pairs[pair]
        newPair2 = pairs[pair] + pair[1]
        
        newPairCounts[newPair1] = newPairCounts.get(newPair1, 0) + count
        newPairCounts[newPair2] = newPairCounts.get(newPair2, 0) + count
        
    return newPairCounts

pairCounts = {}
for i in range(1, len(currentString)):
    pair = currentString[i-1: i + 1]
    pairCounts[pair] = pairCounts.get(pair, 0) + 1

for i in range(40):
    pairCounts = nextIteration(pairCounts)

letterCounts = {}

for i, (pair, count) in enumerate(pairCounts.items()):
    if i==0: letterCounts[pair[0]] = 1
    letterCounts[pair[1]] = letterCounts.get(pair[1], 0) + count

print(f"The answer is {max(letterCounts.values()) - min(letterCounts.values())}")