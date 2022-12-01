reindeer = [0]
with open("input.txt") as file:
    for line in file.readlines():
        if line.strip() == "":
            if len(reindeer) > 3:
                reindeer.remove(min(reindeer))
            reindeer.append(0)
            continue
        reindeer[-1] += int(line)

reindeer.remove(min(reindeer))
print(f"The answer is {sum(reindeer)}")