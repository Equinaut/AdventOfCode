def main():
    connections = dict()
    with open("input.txt") as file:
        for line in file:
            start, others = line[:-1].split(": ")
            connections[start] = tuple(others.split(" "))

    visitCounts = {("svr", False, False): 1}
    ans = 0
    while visitCounts:
        newCounts = dict()
        for (node, a, b), count in visitCounts.items():
            for newNode in connections.get(node, []):
                newState = (newNode, (a or newNode == "dac"), (b or newNode == "fft"))
                newCounts[newState] = newCounts.get(newState, 0) + count
        visitCounts = newCounts
        ans += visitCounts.get(("out", True, True), 0)
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
