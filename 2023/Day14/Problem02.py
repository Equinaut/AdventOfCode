def main():
    ans = 0
    with open("input.txt") as file:
        roundRocks = set()
        cubeRocks = set()

        for y, line in enumerate(file):
            for x, c in enumerate(line[:-1]):
                if c == "#": cubeRocks.add((x, y))
                elif c == "O": roundRocks.add((x, y))
            width = x + 1
        height = y + 1
    
    seen = dict()
    i = 0
    LIMIT = 1_000_000_000
    while i < LIMIT:
        state = stringGrid(width, height, roundRocks, cubeRocks)
        if state in seen: 
            diff = i - seen[state]
            togo = LIMIT - i
            steps = togo // diff
            if steps > 0 and i + diff * steps <= LIMIT:
                seen[state] = i
                i += diff * steps
                continue

        seen[state] = i
        roundRocks = moveDirection(width, height, roundRocks, cubeRocks, (0, -1))
        roundRocks = moveDirection(width, height, roundRocks, cubeRocks, (-1, 0))
        roundRocks = moveDirection(width, height, roundRocks, cubeRocks, (0, 1))
        roundRocks = moveDirection(width, height, roundRocks, cubeRocks, (1, 0))
        i += 1

    ans = sum(height - y for (x, y) in roundRocks)
    return ans

moveCache = dict()
def moveDirection(width, height, roundRocks, cubeRocks, direction):
    prevState = None
    state = None
    i = 0
    startState = stringGrid(width, height, roundRocks, cubeRocks)
    if (startState, direction) in moveCache: return moveCache[startState, direction]
    while i < 15 or prevState is None or state != prevState:
        roundRocks = moveRocks(width, height, roundRocks, cubeRocks, direction)
        i += 1
        if i < 13: continue
        prevState = state
        state = stringGrid(width, height, roundRocks, cubeRocks)

    moveCache[startState, direction] = roundRocks
    return roundRocks

def moveRocks(width, height, roundRocks, cubeRocks, direction):
    offX, offY = direction
    newRoundRocks = set()
    for (x, y) in roundRocks:
        if y + offY >= 0 and y + offY < height and x + offX >= 0 and x + offX < width and ((x + offX, y + offY) not in newRoundRocks) and ((x + offX, y + offY) not in roundRocks) and ((x + offX, y + offY) not in cubeRocks):
            newRoundRocks.add((x + offX, y + offY))
        else: newRoundRocks.add((x, y))
    return newRoundRocks

def stringGrid(width, height, roundRocks, cubeRocks):
    out = ""
    for y in range(0, height + 1):
        for x in range(0, width + 1):
            if (x, y) in roundRocks: out += "O"
            else: out += "."
    return out

def printGrid(roundRocks, cubeRocks):
    width = max(max(x for (x, y) in roundRocks), max(x for (x, y) in cubeRocks))
    height = max(max(y for (x, y) in roundRocks), max(y for (x, y) in cubeRocks))

    for y in range(0, height + 1):
        for x in range(0, width + 1):
            if (x, y) in roundRocks: print("O", end="")
            elif (x, y) in cubeRocks: print("#", end="")
            else: print(".", end="")
        print()
    print("-" * width)

if __name__ == "__main__":
    print(f"The answer is {main()}")