def main():
    graph = dict()
    with open("input.txt") as file:
        for line in file:
            start, end = line[:-1].split(": ")
            end = end.split(" ")
            for i in [start, *end]:
                if i not in graph: graph[i] = set()
            graph[start] |= set(end)
            for i in end: graph[i].add(start)

    commonPairs = dict()
    for i, startNode in enumerate(graph):
        print(i, len(graph), startNode)
        prev = dijkstra(graph, startNode)
        for n in prev:
            if prev[n] is None: continue
            if (n, prev[n]) not in commonPairs: commonPairs[n, prev[n]] = 1
            else: commonPairs[n, prev[n]] += 1

            if (prev[n], n) not in commonPairs: commonPairs[prev[n], n] = 1
            else: commonPairs[prev[n], n] += 1
    
    connections = sorted(commonPairs, key = commonPairs.get, reverse = True)
    allNodes = set(graph)
    node = list(allNodes)[0]

    for i, d1 in enumerate(connections):
        disconnect(graph, d1)
        for j, d2 in enumerate(connections[:i]):
            disconnect(graph, d2)
            for k, d3 in enumerate(connections[:j]):
                disconnect(graph, d3)
                l = len(countParts(graph, node))
                if l != len(allNodes):
                    return l * (len(allNodes) - l)
                connect(graph, d3)
            connect(graph, d2)
        connect(graph, d1)

def disconnect(graph, connection):
    if connection[0] in graph and connection[1] in graph[connection[0]]:
        graph[connection[0]].remove(connection[1])
    if connection[1] in graph and connection[0] in graph[connection[1]]:
        graph[connection[1]].remove(connection[0])

def connect(graph, connection):
    if connection[0] in graph:
        graph[connection[0]].add(connection[1])
    if connection[1] in graph:
        graph[connection[1]].add(connection[0])
    
def countParts(graph, start):
    reached = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node in reached: continue
        reached.add(node)
        queue = queue + list(graph[node])

    return reached    

def dijkstra(graph, start):
    distance = {n: None for n in graph}
    prev = {n: None for n in graph}
    toVisit = {start}
    visited = set()
    distance[start] = 0
    while len(toVisit):
        node = min(toVisit, key = lambda n: distance[n])
        toVisit.remove(node)
        if node in visited: continue
        visited.add(node)

        for nextNode in graph[node]:
            toVisit.add(nextNode)
            if distance[nextNode] is None or distance[node] + 1 < distance[nextNode]:
                distance[nextNode] = 1 + distance[node]
                prev[nextNode] = node
    return prev

if __name__ == "__main__":
    print(f"The answer is {main()}")