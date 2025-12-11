def main():
    connections = dict()
    with open("input.txt") as file:
        for line in file:
            start, others = line[:-1].split(": ")
            connections[start] = tuple(others.split(" "))
    
    visitCounts = {"you": 1}
    ans = 0
    while visitCounts:
        newCounts = dict()
        for node, count in visitCounts.items():
            for newNode in connections.get(node, []):
                newCounts[newNode] = newCounts.get(newNode, 0) + count
        visitCounts = newCounts
        ans += visitCounts.get("out", 0)
    return ans       

if __name__ == "__main__":
    print(f"The answer is {main()}")
