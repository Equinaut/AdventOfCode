def main():
    ans = 0
    grid = []
    with open("input.txt") as file:
        for line in file:
            grid.append(list(line[:-1]))
    
    while True:
        diff = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] != "@": continue
                neighbours = 0
                for (xOff, yOff) in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    newX, newY = (x + xOff, y + yOff)
                    if newX < 0 or newY < 0 or newX >= len(grid[y]) or newY >= len(grid): continue
                    if grid[newY][newX] == "@": 
                        neighbours += 1
                        if neighbours >= 4: break
                else:
                    diff += 1
                    grid[y][x] = "."
        ans += diff
        if diff == 0: break
        print(ans)
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
