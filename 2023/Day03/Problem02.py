def main():
    ans = 0
    with open("input.txt") as file:
        contents = file.readlines()
    chars = set()
    for y, line in enumerate(contents):
        for x, c in enumerate(line):
            if c == "\n": continue
            if c == "*":
                chars.add((x, y))
    
    numPos = dict()

    for (x, y) in chars:
        numPos[x, y] = set()
        for xo in [-1, 0, 1]:
            for yo in [-1, 0, 1]:
                numPos[x, y].add((x + xo, y + yo))

    for (gearX, gearY) in numPos:
        ratios = set()
        for (x, y) in numPos[gearX, gearY]:
            if contents[y][x].isdigit():
                xStart = x
                xEnd = x
                while xStart > 0 and contents[y][xStart -1].isdigit(): xStart -= 1
                while xEnd < len(contents[0]) - 2 and contents[y][xEnd +1].isdigit(): xEnd += 1
                ratios.add((xStart, y, int(contents[y][xStart:xEnd + 1])))
        i = 0
        if len(ratios) == 2:
            i = 1
            for (_,_,r) in ratios: i *= r
        ans += i

    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")