grid = dict()
queue = []
visitedItems = set()

with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        for x, height in enumerate(line[:-1]):
            if height == "E": 
                goal = (x, y)
                height = "z"
            if height == "S": 
                currentPosition = (x, y)
                height = "a"

            grid[x, y] = {
                "height": height, 
                "distance": float('inf'), 
            }
            queue.append((x, y))

grid[currentPosition]["distance"] = 0
queue.remove(currentPosition)
queue.insert(0, currentPosition)

while goal not in visitedItems:
    x, y = queue.pop(0)
    visitedItems.add((x, y))

    for v in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if v in visitedItems: continue
        if v not in grid: continue
        if (ord(grid[v]["height"]) > ord(grid[x, y]["height"]) + 1): continue

        alt = grid[x, y]["distance"] + 1
        if (grid[v]["distance"] is None) or alt < grid[v]["distance"]:
            grid[v]["distance"] = alt
            queue.remove(v)
            i = 0
            while grid[v]["distance"] > grid[queue[i]]["distance"]: i += 1
            queue.insert(i, v)

answer = grid[goal]["distance"]
print(f"The answer is {answer}")