def main():
    ans = 0
    with open("input.txt") as file:
        shapeSizes = dict()
        for i, section in enumerate(file.read().split("\n\n")):
            if "x" in section: 
                for row in section.split("\n")[:-1]:
                    area = (lambda vs: (int(vs[0]) * int(vs[1])))(row.split(": ")[0].split("x"))
                    shapeCounts = tuple(map(int, row.split(": ")[1].split(" ")))
                    if sum(shapeSizes[i] * c for (i, c) in enumerate(shapeCounts)) <= area: ans += 1
            else: shapeSizes[i] = section.count("#")
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")

