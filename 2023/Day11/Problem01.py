def main():
    galaxies = set()
    emptyRows = set()
    emptyCols = []
    with open("input.txt") as file:
        for y, line in enumerate(file):
            if y == 0: emptyCols = [True] * len(line)
            emptyRow = True
            for x, c in enumerate(line):
                if c == "#":
                    galaxies.add((x, y))
                    emptyRow = False
                    emptyCols[x] = False
            if emptyRow: emptyRows.add(y)
    emptyCols = [i for i, t in enumerate(emptyCols) if t]

    for eRow in sorted(emptyRows, reverse=True):
        galaxies = [(x, y + 1 if y >= eRow else y) for (x, y) in galaxies]
    for eCol in sorted(emptyCols, reverse=True):
        galaxies = [(x + 1 if x >= eCol else x, y) for (x, y) in galaxies]

    ans = 0
    for i, g1 in enumerate(galaxies):
        for j, g2 in enumerate(galaxies):
            if j >= i: continue
            ans += abs(g1[1] - g2[1]) + abs(g2[0] - g1[0])
    
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")