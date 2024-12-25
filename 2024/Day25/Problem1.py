def main():
    locks = []
    keys = []
    heights = [-1] * 5
    with open("input.txt") as file:
        for item in file.read().split("\n\n"):
            rows = item.split("\n")
            heights = [-1] * 5
            for row in item.split("\n"):
                for x, c in enumerate(row):
                    if c == "#": heights[x] += 1
            if rows[0] == "#####": locks.append(heights)
            else: keys.append(heights)
    return sum(1 for lock in locks for key in keys if all(l + k <= 5 for l, k in zip(lock, key)))

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")