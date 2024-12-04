def main(diagonalWord):
    ans = 0
    with open("input.txt") as file:
        lines = file.readlines()
        width, height = len(lines[0]), len(lines)

        for y in range(0, height - len(diagonalWord) + 1):
            for x in range(0, width - len(diagonalWord) + 1):
                word1 = "".join([lines[y + i][x + i] for i in range(len(diagonalWord))])
                word2 = "".join([lines[y + i][x + len(diagonalWord) - 1 - i] for i in range(len(diagonalWord))])
                if (word1 == diagonalWord or word1 == diagonalWord[::-1]) and (word2 == diagonalWord or word2 == diagonalWord[::-1]): 
                    ans += 1
    return ans

if __name__ == "__main__":
    ans = main("MAS")
    print(f"The answer is {ans}")