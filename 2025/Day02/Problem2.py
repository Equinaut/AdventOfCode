def main():
    # Get sorted lists of range starts and range ends
    rangeStarts, rangeEnds = [], []
    with open("input.txt") as file:
        line = file.read()
        for r in line.split(","):
            rangeStarts.append(int(r.split("-")[0]))
            rangeEnds.append(int(r.split("-")[1]))
            
    rangeStarts.sort()
    rangeEnds.sort()

    invalidIds = set()
    repeats = 2
    # Increment repeats until it is > than length of longest possible value
    while repeats <= len(str(rangeEnds[-1])):
        startPos = endPos = 0
        i = 1
        # Continue until value is greater than the maximum range end value
        while endPos < len(rangeEnds):
            v = int(str(i) * repeats)
            while startPos < len(rangeStarts) and v >= rangeStarts[startPos]: startPos += 1
            while endPos < len(rangeEnds) and v > rangeEnds[endPos]: endPos += 1
            if startPos > endPos: invalidIds.add(v)
            i += 1
        repeats += 1
    return sum(invalidIds)

if __name__ == "__main__":
    print(f"The answer is {main()}")
