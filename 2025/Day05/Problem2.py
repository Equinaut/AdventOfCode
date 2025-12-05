def main():
    # Load fresh ingredient ranges
    freshRanges = []
    with open("input.txt") as file:
        while (line := file.readline()) != "\n":
            freshRanges.append(tuple(map(int, line[:-1].split("-"))))

    # Sort by start value
    freshRanges.sort(key = lambda a: a[0])

    # Go through all other ranges and update (start, stop) values
    start, stop = freshRanges[0]
    ans = 0
    for a, b in freshRanges[1:]:
        if a <= stop: 
            # Next range overlaps with current, so update end value
            stop = max(stop, b)
        else:
            # New range doesn't overlap, so create new range
            ans += stop - start + 1
            start, stop = a, b
    ans += stop - start + 1
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
