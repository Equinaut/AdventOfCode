def calculateScore(char):
    if ord(char) >= 93: return ord(char) - 96
    if ord(char) >= 65: return ord(char) - 38

def findItem(line):
    firstHalf, secondHalf = line[:int(len(line) / 2)], line[int((len(line) / 2)):]
    return calculateScore(list(set(firstHalf).intersection(secondHalf))[0])

answer = 0
with open("input.txt") as file:
    for line in file.readlines():
        answer += findItem(line[:-1])

print(f"The answer is {answer}")