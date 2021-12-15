grid = []
nodes = []

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.distance = 10000
        self.previous = None
        self.visited = False
        self.neighbours = []
    
    def __repr__(self):
        return f"Node{self.x, self.y, self.value}"


with open("input.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        grid.append([])
        for x, value in enumerate(line[:-1]):
            grid[-1].append(Node(x, y, int(value)))

for y, line in enumerate(grid):
    for x, node in enumerate(line): 
        if y < len(grid)-1: node.neighbours.append(grid[y+1][x])
        if x < len(grid[0])-1: node.neighbours.append(grid[y][x+1])
        if y > 0: node.neighbours.append(grid[y-1][x])
        if x > 0: node.neighbours.append(grid[y][x-1])
        nodes.append(node)

nodes[0].distance = 0

while nodes:
    nodes.sort(key = (lambda node: node.distance))
    thisNode = nodes.pop(0)

    thisNode.visited = True
    for neighbour in thisNode.neighbours:
        if neighbour.visited: continue
        alt = thisNode.distance + neighbour.value
        if alt < neighbour.distance:
            neighbour.distance = alt
            neighbour.previous = thisNode

print(f"The answer is {grid[-1][-1].distance}")
