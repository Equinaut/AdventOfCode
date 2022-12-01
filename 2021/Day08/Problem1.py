answer = 0
segments = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        segments.extend(line[:-1].split(" | ")[1].split(" "))

for segment in segments:
    if len(segment) == 2: answer += 1
    if len(segment) == 4: answer += 1
    if len(segment) == 3: answer += 1
    if len(segment) == 7: answer += 1

print(f"The answer is {answer}")    