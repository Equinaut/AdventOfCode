def main():
    with open("input.txt") as file:
        # Get start position from the first line
        positions = { file.readline().index("S"): 1 }
        for line in file:
            # Update number of ways of reaching each position, for each line in the input
            newPositions = dict()
            for p, c in positions.items():
                if line[p] == "^":
                    newPositions[p - 1] = newPositions.get(p - 1, 0) + c
                    newPositions[p + 1] = newPositions.get(p + 1, 0) + c
                else:
                    newPositions[p] = newPositions.get(p, 0) + c

            positions = newPositions
    # Final result is the number of ways of reaching each possible end position
    return sum(positions.values())

if __name__ == "__main__":
    print(f"The answer is {main()}")
