def main():
    ans = 0
    with open("input.txt") as file:
        d = 50
        for line in file:
            val = int(line[1:])
            if line[0] == "R":
                val -= 100 - d
                ans += 1 + val // 100
                d = val % 100
            elif line[0] == "L":
                val -= d
                if d > 0: ans += 1
                ans += val // 100
                d = (-val) % 100
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
