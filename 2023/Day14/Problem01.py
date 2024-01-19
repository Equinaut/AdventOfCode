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
    
    prevState = None
    state = None
    while prevState is None or state != prevState:
        roundRocks = moveRocksNorth(roundRocks, cubeRocks)
        prevState = state
        state = stringGrid(width, height, roundRocks, cubeRocks)

    for (x, y) in roundRocks:
        ans += height - y
    return ans

def moveRocksNorth(roundRocks, cubeRocks):
    newRoundRocks = set()
    for (x, y) in roundRocks:
        if y - 1 >= 0 and ((x, y - 1) not in newRoundRocks) and ((x, y - 1) not in roundRocks) and ((x, y - 1) not in cubeRocks):
            newRoundRocks.add((x, y - 1))
        else:
            newRoundRocks.add((x, y))
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

    for y in range(0, height):
        for x in range(0, width):
            if (x, y) in roundRocks: print("O", end="")
            elif (x, y) in cubeRocks: print("#", end="")
            else: print(".", end="")
        print()
    print("-" * width)

if __name__ == "__main__":
    print(f"The answer is {main()}")