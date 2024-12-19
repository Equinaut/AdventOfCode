def testPattern(target, patterns):
    if target == "": return True
    for p in patterns:
        if target.startswith(p):
            if testPattern(target[len(p):], patterns): return True
    return False

def main():
    with open("input.txt") as file:
        patterns = set(file.readline()[:-1].split(", "))
        file.readline()
        targets = []
        while (line := file.readline()):
            targets.append(line[:-1])
            
    return sum(1 for t in targets if testPattern(t, patterns))

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")