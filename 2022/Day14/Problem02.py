filled = set()
maxY = 0

def getFilled(x, y): return y >= maxY + 2 or (x, y) in filled

with open("input.txt") as file:
    for line in file.readlines():
        path = list(map(lambda p : list(map(int,p.split(","))) ,line.split(" -> ")))
        for i in range(0, len(path) - 1):
            s = path[i]
            e = path[i + 1]
            for x in range(min(s[0], e[0]), max(s[0], e[0]) + 1):
                for y in range(min(s[1], e[1]), max(s[1], e[1]) + 1):
                    filled.add((x, y))
                    if y > maxY: maxY = y

def addSand(x, y):
    if getFilled(500, 0): return None
    if not getFilled(x,     y + 1): return addSand(x,     y + 1)
    if not getFilled(x - 1, y + 1): return addSand(x - 1, y + 1)
    if not getFilled(x + 1, y + 1): return addSand(x + 1, y + 1)
    filled.add((x, y))
    return x, y

answer = 0
while addSand(500, 0) is not None: answer += 1

print(f"The answer is {answer}")