def solveMachine(machine):
    x1, y1, x2, y2, targetX, targetY = machine
    b = (((targetY * x1) - (targetX * y1)) / ((y2 * x1) - (x2 * y1)))
    a = (targetX - (b * x2)) / x1
    if a % 1 > 0 or b % 1 > 0 or a < 0 or b < 0: return 0
    return int(a * 3 + b)

def main():
    machines = []
    with open("input.txt") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            x1, y1 = (int(j.split("+")[1]) for j in lines[i][:-1].split(": ")[1].split(", "))
            x2, y2 = (int(j.split("+")[1]) for j in lines[i + 1][:-1].split(": ")[1].split(", "))
            xTarget, yTarget = (int(j.split("=")[1]) for j in lines[i + 2][:-1].split(": ")[1].split(", "))
            machines.append((x1, y1, x2, y2, xTarget, yTarget))

    ans = 0
    for x1, y1, x2, y2, targetX, targetY in machines:
        ans += solveMachine((x1, y1, x2, y2, targetX, targetY))
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")