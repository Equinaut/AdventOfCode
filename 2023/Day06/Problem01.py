def main():
    with open("input.txt") as file:
        times = [int(i) for i in file.readline().split(": ")[1].split(" ") if len(i)]
        distances = [int(i) for i in file.readline().split(": ")[1].split(" ") if len(i)]

    ans = 1
    for t, d in zip(times, distances):
        ways = 0
        for i in range(0, t):
            if (t - i) * i > d: ways += 1
        ans *= ways
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")