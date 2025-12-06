def main():
    grid = []
    with open("input.txt") as file:
        lines = file.readlines()
        column = []
        for i in range(0, len(lines[0]) - 1):
            currentNumber = "".join(lines[j][i] for j in range(0, len(lines) - 1))
            if len(currentNumber.strip()) == 0: 
                grid.append(column)
                column = []
            else: column.append(int(currentNumber))
    grid.append(column)

    ans = 0
    for i, op in enumerate(lines[-1].split()):
        if op == "*":
            product = 1
            for v in grid[i]: product *= v
            ans += product
        elif op == "+":
            ans += sum(grid[i])
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
