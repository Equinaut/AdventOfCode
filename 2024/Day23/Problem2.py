
def main():
    connections = dict()
    with open("input.txt") as file:
        for line in file:
            a, b = line[:-1].split("-")
            if a not in connections: connections[a] = { a }
            if b not in connections: connections[b] = { b }
            connections[a].add(b)
            connections[b].add(a)
    
    queue = []
    for c in connections: queue.append(((c,), connections[c]))

    largestSet = set()
    while queue:
        compSet, nextSet = queue.pop(0)
        if len(compSet) > len(largestSet):
            largestSet = set([c for c in compSet])

        for nextItem in connections[compSet[-1]]:
            if nextItem <= compSet[-1]: continue
            newNextSet = nextSet & connections[nextItem]
            if not all(currentItem in newNextSet for currentItem in compSet): continue
            queue.append(((*compSet, nextItem), newNextSet))

    return ",".join(sorted(compSet))

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")