directions = [(1, 0), (0, 1), (-1, 0), (0, -1),]

def solveGrid(grid, pointCount):
    width, height = len(grid[0]), len(grid)
    queue = [(0, 0, 0),]
    visited = set()
    while queue:
        (t, x, y) = queue.pop(0)
        visited.add((x, y))
        
        if (x, y) == (width - 1, height - 1): return t

        for xOff, yOff in directions:
            newX = x + xOff
            newY = y + yOff

            if newX < 0 or newY < 0 or newX >= width or newY >= height: continue
            if grid[newY][newX] is not None and grid[newY][newX] <= pointCount: continue

            if (newX, newY) in visited: continue
            visited.add((newX, newY))
            queue.append((t + 1, newX, newY))
    return None

def main():
    coords = []
    with open("input.txt") as file:
        width, height = 0, 0
        for i, line in enumerate(file):
            x, y = line[:-1].split(",")
            coords.append((int(x), int(y)))
            width = max(width, int(x))
            height = max(height, int(y))

        grid = [[None] * (width + 1) for _ in range(height + 1)]
        for i, (x, y) in enumerate(coords): grid[y][x] = i
    return solveGrid(grid, 1024)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")