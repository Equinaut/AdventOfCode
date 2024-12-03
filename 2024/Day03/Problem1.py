import re

def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            for calc in re.findall("mul\(\d+,\d+\)", line):
                a, b = calc[4:-1].split(",")
                ans += int(a) * int(b)
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")