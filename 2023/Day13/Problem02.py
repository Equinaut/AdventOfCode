import copy

def main():
    grids = [[[]]]
    with open("input.txt") as file:
        for line in file:
            if line == "\n": grids.append([[]])
            else:
                grids[-1][-1] = list(line[:-1])
                grids[-1].append([])

    ans = sum(findSmudgeReflection(grid[:-1]) for grid in grids)
    return ans

def findSmudgeReflection(grid):
    defaultReflection = findRelections(grid)
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            newGrid = copy.deepcopy(grid)
            if newGrid[y][x] == ".": newGrid[y][x] = "#"
            else: newGrid[y][x] = "."
            r = findRelections(newGrid)
            if defaultReflection[0] in r: r.remove(defaultReflection[0])
            if r: return r[0]

def findRelections(grid):
    reflections = []
    for x in range(1, len(grid[0])):
        width = min(x, len(grid[0]) - x)
        left = [line[x-width:x] for line in grid]
        right = [line[x:x+width][::-1] for line in grid]
        if all(l == r for l, r in zip(left, right)): reflections.append(x)
        
    for y in range(1, len(grid)):
        height = min(y, len(grid) - y)
        top = grid[y - height : y]
        bottom = grid[y : y + height][::-1]
        if all (t == b for t, b in zip(top, bottom)): reflections.append(y * 100)
    return reflections


if __name__ == "__main__":
    print(f"The answer is {main()}")