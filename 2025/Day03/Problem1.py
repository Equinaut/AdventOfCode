def solveBank(bank):
    out = 0
    for i in range(0, len(bank)):
        for j in range(i + 1, len(bank)):
            out = max(out, int(bank[i] + bank[j]))
    return out

def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            ans += solveBank(line[:-1])
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
