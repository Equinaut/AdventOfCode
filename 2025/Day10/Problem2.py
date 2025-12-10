from z3 import *

def solveCase(joltage, buttons):
    buttonSymbols = Ints(" ".join(str(i) for i in range(0, len(buttons))))
    solver = Optimize()
    for b in buttonSymbols: solver.add(b >= 0)

    sums = [[] for _ in range(0, len(joltage))]
    
    for i, button in enumerate(buttons):
        for v in button: sums[v].append(buttonSymbols[i])

    for s, value in zip(sums, joltage): solver.add(Sum(s) == value)

    ans = Int("ans")
    solver.add(Sum(buttonSymbols) == ans)
    solver.minimize(ans)
    assert(solver.check() == sat)
    return solver.model()[ans].as_long()

def main():
    ans = 0
    machines = []
    with open("input.txt") as file:
        for line in file:
            buttons = []
            joltage = None
            for section in line[:-1].split(" "):
                if section[0] == "(": buttons.append(tuple(map(int, section[1:-1].split(","))))
                elif section[0] == "{": joltage = tuple(map(int, section[1:-1].split(",")))
            machines.append((buttons, joltage))

    for i, (buttons, joltage) in enumerate(machines):
        ans += solveCase(tuple(joltage), tuple(buttons))
        print(f"({i} / {len(machines)}) - {ans} \t {joltage}")
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
