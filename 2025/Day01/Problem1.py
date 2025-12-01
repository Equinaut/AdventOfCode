def main():
    ans = 0
    with open("input.txt") as file:
        d = 50
        for line in file:
            val = int(line[1:])
            if line[0] == "R": d += val
            elif line[0] == "L": d -= val
            d %= 100
            if d % 100 == 0: ans += 1
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
