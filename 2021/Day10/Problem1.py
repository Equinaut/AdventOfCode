lines = []
with open("input.txt", "r") as file:
    for line in file.readlines(): lines.append(line[:-1])

validPairs = ["()", "[]", "{}", "<>"]
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
answer = 0

for i, line in enumerate(lines):
    while validPairs[0] in lines[i] or validPairs[1] in lines[i] or validPairs[2] in lines[i] or validPairs[3] in lines[i]:
        for j in validPairs:
            if j in lines[i]: lines[i] = lines[i].replace(j, "")

    anyClosing = False
    for char in lines[i]:
        if char in points: 
            anyClosing = True
            break
    if anyClosing: 
        print(lines[i], char)
        answer += points[char]

print(f"The answer is {answer}")