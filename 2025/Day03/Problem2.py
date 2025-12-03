def solveBank(bank, c):
    out = 0
    lastIndex = -1
    while c > 0:
        maxDigit = -1
        for i in range(lastIndex + 1, len(bank) -c + 1):
            if int(bank[i]) > maxDigit:
                maxDigit = int(bank[i])
                lastIndex = i
        out = (out * 10 + maxDigit)
        c -= 1
    return out

def main():
    ans = 0
    with open("input.txt") as file: ans = sum(solveBank(line[:-1], 12) for line in file)
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
