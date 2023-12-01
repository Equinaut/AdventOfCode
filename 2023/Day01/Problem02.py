digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            first = last = None
            for i in range(0, len(line)):
                for digit in digits:
                    if line[i:].startswith(digit) and first is None:
                        first = digits[digit]

                    if line[:len(line)-i].endswith(digit) and last is None:
                        last = digits[digit]

                if line[i].isdigit() and first is None: 
                    first = line[i]

                if line[-i - 1].isdigit() and last is None: 
                    last = line[-i - 1]
            
            ans += int(first) * 10 + int(last)
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")
