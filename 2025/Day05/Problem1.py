def main():
    freshRanges = []
    ans = 0
    with open("input.txt") as file:
        while (line := file.readline()) != "\n":
            # Add all ranges of fresh ingredients to a list
            freshRanges.append(tuple(map(int, line[:-1].split("-"))))

        while (line := file.readline()):
            v = int(line[:-1])
            # Check v against the ranges of fresh ingredients
            if any(v >= r[0] and v <= r[1] for r in freshRanges): ans += 1
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
