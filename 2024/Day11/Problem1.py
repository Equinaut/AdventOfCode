def blink(numbers):
    newNumbers = []
    for n in numbers:
        if n == 0: newNumbers.append(1)
        elif len(str(n)) % 2 == 0:
            l = len(str(n))
            newNumbers.append(int(str(n)[ :l // 2]))
            newNumbers.append(int(str(n)[l // 2: ]))
        else:
            newNumbers.append(n * 2024)
    return newNumbers

def main():
    with open("input.txt") as file:
        numbers = list(map(int, file.read().split(" ")))
    for _ in range(25): numbers = blink(numbers)
    return len(numbers)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")