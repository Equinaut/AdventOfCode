def calculateScore(char):
    if ord(char) >= 93: return ord(char) - 96
    if ord(char) >= 65: return ord(char) - 38

def getBadge(line1, line2, line3):
    return list(set(line1).intersection(line2).intersection(line3))[0]

answer = 0
with open("input.txt") as file:
    lines = file.readlines()
    while len(lines):
        line1 = lines.pop(0).strip()
        line2 = lines.pop(0).strip()
        line3 = lines.pop(0).strip()
        answer += calculateScore(getBadge(line1, line2, line3))

print(f"The answer is {answer}")