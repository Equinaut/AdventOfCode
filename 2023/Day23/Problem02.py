def main():
    paths = set()
    start = None
    with open("input.txt") as file:
        for y, line in enumerate(file):
            for x, c in enumerate(line):
                if c == "." or c == ">" or c == "<" or c == "^" or c == "v": 
                    paths.add((x, y))
                    if y == 0: start = (x, y)
    end = max(paths, key = lambda a: a[1])
    
    # Build initial graph, which contains all nodes
    graph = dict()
    for p in paths:
        graph[p] = set()
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newPos = (p[0] + d[0], p[1] + d[1])
            dist = 1
            if newPos not in paths: continue
            graph[p].add((newPos, dist))
    
    # Find corner nodes, these are defined as nodes that have != 2 neighbours
    corners = set()
    for n in graph:
        if len(graph[n]) != 2:
            corners.add(n)
        
    # Construct a smaller graph using just the corner nodes
    simpleGraph = {c: set() for c in corners}
    for c in corners:
        for c2 in corners:
            d = findDistance(c, c2, graph)
            if d is None: continue
            simpleGraph[c].add((c2, d))

    queue = [(start, 0, set())]
    maxDist = 0
    while queue:
        current, currentDist, visited = queue.pop()
        if current == end and currentDist > maxDist: maxDist = currentDist

        for nextNode, d in simpleGraph[current]:
            if nextNode in visited: continue
            newDist = currentDist + d
            newVisited = {(x, y) for (x, y) in visited} | {nextNode}
            queue.append((nextNode, newDist, newVisited))
    return maxDist

def printGraph(graph, corners):
    width = max(a for (a, b) in graph) + 1
    height = max(b for (a, b) in graph) + 1
    for y in range(0, height + 1):
        for x in range(0, width + 1):
            if (x, y) in corners: print("🟥", end="")
            elif (x, y) in graph: print("⬛", end="")
            else: print("⬜", end="")
        print()

def findDistance(c1, c2, graph):
    if c1 == c2: return None
    for first, dist in graph[c1]:
        visited = {c1, first}
        current = first
        while current != c2:
            current, d = [(n, d) for (n, d) in graph[current] if n not in visited][0]
            dist += d
            if current == c2: return dist
            if len(graph[current]) != 2: break
            visited.add(current)

if __name__ == "__main__":
    print(f"The answer is {main()}")