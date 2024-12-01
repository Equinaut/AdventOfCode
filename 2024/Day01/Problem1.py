def main():
    ans = 0
    l1, l2 = [], []
    with open("input.txt") as file:
        for line in file:
            a, b = line.split("   ")
            a = int(a)
            b = int(b)
            l1.append(a)
            l2.append(b)
    l1.sort()
    l2.sort()
    for a, b in zip(l1, l2): ans += abs(a - b)

    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")