def main():
    with open("input.txt") as file:
        time = int(file.readline()[:-1].split(": ")[1].replace(" ", ""))
        distance = int(file.readline()[:-1].split(": ")[1].replace(" ", ""))

    ans = 0
    for i in range(0, time):
        if i % 1000000 == 0: print(i / time)
        if (time - i) * i > distance:
            ans += 1
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")