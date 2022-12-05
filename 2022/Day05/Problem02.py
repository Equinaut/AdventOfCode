stacks = []

def move(amount, start, end):
    toMove = stacks[start - 1][:amount]
    stacks[start - 1] = stacks[start - 1][amount:]
    stacks[end - 1] = toMove + stacks[end - 1]

loadstacks = True

with open("input.txt") as file:
    for line in file.readlines():
        if line == "\n": 
            loadstacks = False
            continue
        if loadstacks:
            line = line[:-1]
            for i,l in enumerate(line[1::2]):
                if l.isdigit(): break
                if l != " ":
                    while len(stacks) <= i//2: stacks.append([])
                    stacks[i//2].append(l)
        else:
            move(*map(int, line[:-1].split(" ")[1::2]))

answer = ""
for stack in stacks:
    answer = answer + stack[0]
    
print(f"The answer is {answer}")