def process(n):
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    return n 

def getAllSequences(n, iterationCount):
    vals = []
    changes = []
    seen = set()
    for _ in range(iterationCount):
        new = process(n)
        vals.append((new % 10) - (n % 10))
        vals = vals[-4:]
        if tuple(vals) not in seen: 
            changes.append((tuple(vals), new % 10))
        seen.add(tuple(vals))
        n = new
    return changes

def main():
    with open("input.txt") as file:
        nums = [int(line[:-1]) for line in file.readlines()]
    sequenceValues = dict()
    for i, n in enumerate(nums):
        if i % 500 == 0: print(i, len(nums))
        seqs = getAllSequences(n, 2000)
        for seq in seqs:
            if seq[0] not in sequenceValues: sequenceValues[seq[0]] = 0
            sequenceValues[seq[0]] += seq[1]
    return max(sequenceValues.values())

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")