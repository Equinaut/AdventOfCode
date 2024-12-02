def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            values = list(map(int, line.split(" ")))
            allInc, allDec = True, True
            for i in range(1, len(values)):
                diff = values[i] - values[i - 1]
                if diff < 1 or diff > 3: allInc = False
                if diff > -1 or diff < -3: allDec = False
            if allInc or allDec: ans += 1
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")