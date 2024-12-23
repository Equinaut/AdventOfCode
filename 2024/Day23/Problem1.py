
def main():
    ans = 0
    connections = dict()
    with open("input.txt") as file:
        for line in file:
            a, b = line[:-1].split("-")
            if a not in connections:
                connections[a] = {a}
            if b not in connections:
                connections[b] = {b}

            connections[a].add(b)
            connections[b].add(a)
    ans = 0 
    for a in connections:
        if a[0] != "t": continue
        for b in connections[a]:
            for c in connections[b]:
                if c <= b: continue
                fullSet = connections[a] & connections[b] & connections[c]
                if a == b or a == c: continue
                if b[0] == "t" and b <= a: continue
                if c[0] == "t" and c <= a: continue
                if a in fullSet and b in fullSet and c in fullSet:
                    print(a,b,c)
                    ans += 1
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")