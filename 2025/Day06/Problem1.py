def main():
    grid = []
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines[:-1]:
            grid.append(tuple([int(n) for n in line[:-1].split()]))
    
    ans = 0
    for i, op in enumerate(lines[-1][:-1].split()):
        if op == "*":
            product = 1
            for j in range(0, len(grid)): product *= grid[j][i]
            ans += product
        elif op == "+":
            ans += sum(grid[j][i] for j in range(0, len(grid)))
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
