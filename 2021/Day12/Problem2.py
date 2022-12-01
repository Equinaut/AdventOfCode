connections = dict()
paths = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        start, end = line[:-1].split("-")
        if start in connections and end != "start": connections[start].append(end)
        elif end != "start": connections[start] = [end]

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
    if not currentPath[-1] in connections:
        return
    for destinationNode in connections[currentPath[-1]]:
        if destinationNode == destinationNode.upper() or (not currentPath[0]) or (not destinationNode in currentPath):
            repeatSmallCave = currentPath[0]
            if destinationNode == destinationNode.lower() and destinationNode in currentPath: repeatSmallCave = True

            findPath([repeatSmallCave] + currentPath[1:] + [destinationNode])

findPath([False, "start"])

print(f"The answer is {len(paths)}")
