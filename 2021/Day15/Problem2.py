subgrid = []
subGridWidth = subGridHeight = 0
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
        subgrid.append([])
        for x, value in enumerate(line[:-1]):
            subgrid[-1].append(Node(x, y, int(value)))

subGridWidth, subGridHeight = len(subgrid[0]), len(subgrid)
grid = [[None for _ in range(subGridWidth * 5)] for _ in range(subGridHeight * 5)]

for bigX in range(0, 5):
    for bigY in range(0, 5):
        for y, line in enumerate(subgrid):
            for x, node in enumerate(line):
                newValue = node.value + bigX + bigY
                while newValue > 9: newValue-=9
                grid[bigY * subGridHeight + y][bigX * subGridHeight + x] = Node(node.x, node.y, newValue)

for y, line in enumerate(grid):
    for x, node in enumerate(line): 
        if y < len(grid)-1: node.neighbours.append(grid[y+1][x])
        if x < len(grid[0])-1: node.neighbours.append(grid[y][x+1])
        if y > 0: node.neighbours.append(grid[y-1][x])
        if x > 0: node.neighbours.append(grid[y][x-1])
        nodes.append(node)

nodes[0].distance = 0
nodes[-1].neighbours = []

while nodes:
    if len(nodes)%10000==0: print(len(nodes))
        
    thisNode = nodes.pop(0)
    
    thisNode.visited = True
    for neighbour in thisNode.neighbours:
        if neighbour.visited: continue
        alt = thisNode.distance + neighbour.value
        if alt < neighbour.distance:
            neighbour.distance = alt
            neighbour.previous = thisNode
            nodes.remove(neighbour)

            i=0
            while i<len(nodes) and nodes[i].distance < neighbour.distance: i+=1
            nodes.insert(i, neighbour)

print(f"The answer is {grid[-1][-1].distance}")