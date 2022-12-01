lines = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line[:-1])

validPairs = ["()", "[]", "{}", "<>"]
matchingPair = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
repairScores = []


def calculateScore(repairString):
    score = 0
    for char in repairString:
        score *= 5
        if char == ")":
            score += 1
        elif char == "]":
            score += 2
        elif char == "}":
            score += 3
        elif char == ">":
            score += 4
    return score

for i, line in enumerate(lines):
    while validPairs[0] in lines[i] or validPairs[1] in lines[i] or validPairs[2] in lines[i] or validPairs[3] in lines[i]:
        for j in validPairs:
            if j in lines[i]:
                lines[i] = lines[i].replace(j, "")

    for char in lines[i]:
        if char in points:
            lines[i] = None

while None in lines: lines.remove(None)

for i, line in enumerate(lines):
    repairString = ""
    while not lines[i] == "":
        repairString = repairString + matchingPair[lines[i][-1]]
        lines[i] = lines[i] + matchingPair[lines[i][-1]]
        while validPairs[0] in lines[i] or validPairs[1] in lines[i] or validPairs[2] in lines[i] or validPairs[3] in lines[i]:
            for validPair in validPairs: 
                if validPair in lines[i]: lines[i] = lines[i].replace(validPair, "")
    repairScores.append(calculateScore(repairString))

repairScores.sort()
print(f"The answer is {repairScores[len(repairScores)//2]}")
