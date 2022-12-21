filled = set()

with open("input.txt") as file:
    for line in file.readlines():
        path = list(map(lambda p : list(map(int,p.split(","))) ,line.split(" -> ")))

        for i, s in enumerate(path[:-1]):
            e = path[i + 1]
            for x in range(min(s[0], e[0]), max(s[0], e[0]) + 1):
                for y in range(min(s[1], e[1]), max(s[1], e[1]) + 1):
                    filled.add((x, y))

def addSand(x, y):
    if y > 500: return None
    if not (x    , y + 1) in filled: return addSand(x,     y + 1)
    if not (x - 1, y + 1) in filled: return addSand(x - 1, y + 1)
    if not (x + 1, y + 1) in filled: return addSand(x + 1, y + 1)
    filled.add((x, y))
    return x, y

answer = 0
while addSand(500, 0) is not None: answer += 1

print(f"The answer is {answer}")