def main(redMax, greenMax, blueMax):
    ans = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.split(": ")
            num = int(line[0].split(" ")[1])
            for revealedSet in line[1].split("; "):
                r = g = b = 0

                for revealed in revealedSet.split(", "):
                    n = int(revealed.split(" ")[0])
                    c = revealed.split(" ")[1]
                    if c[0] == "r": r += n
                    if c[0] == "g": g += n
                    if c[0] == "b": b += n
                if r > redMax or g > greenMax or b > blueMax: break
            else:
                ans += num
    return ans


if __name__ == "__main__":
    print(f"The answer is {main(12, 13, 14)}")