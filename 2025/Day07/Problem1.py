def main():
    ans = 0
    with open("input.txt") as file:
        # Get start position from the first line
        positions = { file.readline().index("S") }
        for line in file:
            # Update set of reachable positions
            newPositions = set()
            for p in positions:
                if line[p] == "^":
                    newPositions.add(p - 1)
                    newPositions.add(p + 1)
                    # Count number of splits
                    ans += 1
                else:
                    newPositions.add(p)
            positions = newPositions
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
