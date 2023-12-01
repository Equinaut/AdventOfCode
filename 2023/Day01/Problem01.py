def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            first = last = None
            for i in range(0, len(line)):
                if line[i].isdigit() and first is None: 
                    first = line[i]

                if line[-i - 1].isdigit() and last is None: 
                    last = line[-i - 1]

            ans += int(first) * 10 + int(last) 
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")