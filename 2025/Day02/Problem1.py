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
    
    ans = 0
    startPos = endPos = 0
    i = 1
    while endPos < len(rangeEnds):
        v = int(str(i) + str(i))
        while startPos < len(rangeStarts) and v >= rangeStarts[startPos]: startPos += 1
        while endPos < len(rangeEnds) and v > rangeEnds[endPos]: endPos += 1
        if startPos > endPos: ans += v
        i += 1
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
