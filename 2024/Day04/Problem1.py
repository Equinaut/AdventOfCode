def main(searchWord):
    ans = 0
    with open("input.txt") as file:
        lines = file.readlines()
        width, height = len(lines[0]), len(lines)

        for y in range(0, len(lines)):
            for x in range(0, len(lines[0])):
                checkWords = []
                if x + len(searchWord) <= width: 
                    checkWords.append("".join([lines[y][x + i] for i in range(len(searchWord))]))

                if y + len(searchWord) <= height: 
                    checkWords.append("".join([lines[y + i][x] for i in range(len(searchWord))]))

                if y + len(searchWord) <= height and x + len(searchWord) <= width: 
                    checkWords.append("".join([lines[y + i][x + i] for i in range(len(searchWord))]))

                if y >= (len(searchWord) - 1) and x + len(searchWord) <= height: 
                    checkWords.append("".join([lines[y - i][x + i] for i in range(len(searchWord))]))

                ans += checkWords.count(searchWord) + checkWords.count(searchWord[::-1])
    return ans

if __name__ == "__main__":
    ans = main("XMAS")
    print(f"The answer is {ans}")