def main():
    ans = 0
    with open("input.txt") as file:
        contents = file.readlines()
    chars = set()
    for y, line in enumerate(contents):
        for x, c in enumerate(line):
            if c == "\n": continue
            if (not c.isdigit()) and c != ".":
                chars.add((x, y))
    
    numPos = set()

    for (x, y) in chars:
        for xo in [-1, 0, 1]:
            for yo in [-1, 0, 1]:
                numPos.add((x + xo, y + yo))
    nums = set()
    for (x, y) in numPos:
        if contents[y][x].isdigit():
            xStart = x
            xEnd = x
            while xStart > 0 and contents[y][xStart -1].isdigit(): xStart -= 1
            while xEnd < len(contents[0]) - 2 and contents[y][xEnd +1].isdigit(): xEnd += 1
            nums.add((y, xStart, int(contents[y][xStart:xEnd + 1])))

    for __, _, i in nums:
        ans += i
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")