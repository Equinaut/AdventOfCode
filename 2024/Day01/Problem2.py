def main():
    ans = 0
    l1, l2 = [], []
    with open("input.txt") as file:
        for line in file:
            a, b = line.split("   ")
            l1.append(int(a))
            l2.append(int(b))
    l1.sort()
    for a, b in zip(l1, l2): ans += a * l2.count(a)
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")