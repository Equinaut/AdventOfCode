from functools import cache
directions = [(-1, 0, "<", ">"), (1, 0, ">", "<"), (0, -1, "^", "v"), (0, 1, "v", "^")]

numericLayout = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}

sequences = {
    "AA" : "A",
    "A>" : "vA",
    "A<" : "v<<A",
    "Av" : "<vA",
    "A^" : "<A",
    ">A" : "^A",
    ">>" : "A",
    "><" : "<<A",
    ">v" : "<A",
    ">^" : "<^A",
    "<A" : ">>^A",
    "<>" : ">>A",
    "<<" : "A",
    "<v" : ">A",
    "<^" : ">^A",
    "^A" : ">A",
    "^>" : "v>A",
    "^<" : "v<A",
    "^v" : "vA",
    "^^" : "A",
    "vA" : "^>A",
    "v>" : ">A",
    "v<" : "<A",
    "vv" : "A",
    "v^" : "^A",
}


@cache
def countPresses(prev, current, robotsLeft):
    if robotsLeft == 1: return len(sequences[prev + current])    
    seq = "A" + sequences[prev + current]
    return sum(countPresses(seq[i - 1], seq[i], robotsLeft - 1) for i in range(1, len(seq)))

def lastDirectionOptions(numpadValues):
    queue = [((2, 3), "", set(), numpadValues),]
    outpaths = []
    while queue:
        pos, path, visited, remainingInput = queue.pop()
        if len(remainingInput) == 0:
            outpaths.append(path)
            continue

        if numericLayout[pos] == remainingInput[0]:
            queue.append((pos, path + "A", set(), remainingInput[1:]))
            continue

        for offset in directions:
            newPos = (pos[0] + offset[0], pos[1] + offset[1])
            if newPos not in numericLayout: continue
            if newPos in visited: continue
            if path and offset[3] == path[-1]: continue

            queue.append((newPos, path + offset[2], visited | { newPos }, remainingInput))

    minLength = min(map(len, outpaths))
    return [p for p in outpaths if len(p) == minLength]

def main():
    with open("input.txt") as file:
        inputVals = [line[:-1] for line in file.readlines()]

    ans = 0
    for line in inputVals:
        originalOptions = lastDirectionOptions(line)
        lineValue = int("".join(c for c in line if c.isnumeric()))
        fewestPresses = min(sum(countPresses(options[i - 1], options[i], 2) for i in range(len(options))) for options in originalOptions)
        ans += fewestPresses * lineValue

    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")