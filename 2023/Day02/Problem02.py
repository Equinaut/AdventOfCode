def main():
    with open("input.txt") as file:
        ans = 0
        for line in file.readlines():
            line = line.split(": ")
            r = g = b = 0
            for revealedSet in line[1].split("; "):
                for revealed in revealedSet.split(", "):
                    n = int(revealed.split(" ")[0])
                    c = revealed.split(" ")[1]
                    if c[0] == "r": r = max(n, r)
                    if c[0] == "g": g = max(n, g)
                    if c[0] == "b": b = max(n, b)
                
            ans += r * g * b
    return ans


if __name__ == "__main__":
    print(f"The answer is {main()}")