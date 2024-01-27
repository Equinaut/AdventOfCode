def main():
    paths = set()
    slopes = dict()
    start = None
    with open("input.txt") as file:
        for y, line in enumerate(file):
            for x, c in enumerate(line):
                if c == ".": 
                    paths.add((x, y))
                    if y == 0: start = (x, y)
                if c == ">": slopes[(x, y)] = "R"
                if c == "v": slopes[(x, y)] = "D"
                if c == "<": slopes[(x, y)] = "L"
                if c == "^": slopes[(x, y)] = "U"
    
    end = max(paths, key = lambda a: a[1])

    # Construct the graph, following slopes until the next path
    graph = dict()
    for p in paths:
        graph[p] = set()
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newPos = (p[0] + d[0], p[1] + d[1])
            dist = 1
            while newPos in slopes:
                if slopes[newPos] == "R": newPos = (newPos[0] + 1, newPos[1])
                elif slopes[newPos] == "L": newPos = (newPos[0] - 1, newPos[1])
                elif slopes[newPos] == "U": newPos = (newPos[0], newPos[1] - 1)
                elif slopes[newPos] == "D": newPos = (newPos[0], newPos[1] + 1)
                dist += 1
            if newPos not in paths: continue
            graph[p].add((newPos, dist))
    
    # Runs depth first search through the graph to find longest path
    queue = [(start, 0, set())]
    maxDist = 0
    while queue:
        if len(queue) % 100 == 0: print(len(queue))
        current, currentDist, visited = queue.pop()
        if current == end and currentDist > maxDist: maxDist = currentDist
        for nextNode, d in graph[current]:
            if nextNode in visited: continue
            newDist = currentDist + d
            newVisited = {(x, y) for (x, y) in visited} | {nextNode}
            queue.append((nextNode, newDist, newVisited))
    return maxDist

if __name__ == "__main__":
    print(f"The answer is {main()}")