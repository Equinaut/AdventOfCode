def contains(range1, range2):
    return (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1])

answer = 0
with open("input.txt") as file:
    for line in file.readlines():
        pairs = line.split(",")
        ranges = [(int(pair.split("-")[0]), int(pair.split("-")[1])) for pair in pairs]
        if contains(*ranges): answer += 1

print(f"The answer is {answer}")