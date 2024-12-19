cache = dict()
def testPattern(target, patterns):
    if target in cache: return cache[target]
    if target == "": return 1
    ans = 0
    for p in patterns:
        if target.startswith(p):
            ans += testPattern(target[len(p):], patterns)
    cache[target] = ans
    return ans

def main():
    with open("input.txt") as file:
        patterns = set(file.readline()[:-1].split(", "))
        file.readline()
        targets = []
        while (line := file.readline()):
            targets.append(line[:-1])

    return sum(testPattern(t, patterns) for t in targets)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")