def process(n):
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    return n 

def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            n = int(line[:-1])
            for _ in range(2000): n = process(n)
            ans += n
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")