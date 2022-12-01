connections = dict()
paths = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        start, end = line[:-1].split("-")
        if start in connections: connections[start].append(end)
        else: connections[start] = [end]

        start, end = end, start
        if end == "start": continue
        if start == "end": continue
        if start in connections: connections[start].append(end)
        else: connections[start] = [end]

currentNode = "start"

def findPath(currentPath):
    if currentPath[-1] == "end": 
        paths.append(currentPath)
        return
    if not currentPath[-1] in connections: return
    for destinationNode in connections[currentPath[-1]]:
        if destinationNode == destinationNode.upper() or not destinationNode in currentPath:
            findPath(currentPath + [destinationNode])

findPath(["start"])

print(f"The answer is {len(paths)}")