from z3 import *

def main():
    hailstones = list()
    with open("input.txt") as file:
        for line in file:
            x1, y1, z1, xv, yv, zv = list(map(int, line.replace("@", ",").split(",")))
            hailstones.append((x1, y1, z1, xv, yv, zv))
    a,b,c,d,e,f,t1,t2,t3,answer = Ints("a b c d e f t1 t2 t3 answer")
    solver = Solver()
    solver.add(hailstones[0][0] + hailstones[0][3] * t1 == a + b * t1)
    solver.add(hailstones[0][1] + hailstones[0][4] * t1 == c + d * t1)
    solver.add(hailstones[0][2] + hailstones[0][5] * t1 == e + f * t1)
    solver.add(hailstones[1][0] + hailstones[1][3] * t2 == a + b * t2)
    solver.add(hailstones[1][1] + hailstones[1][4] * t2 == c + d * t2)
    solver.add(hailstones[1][2] + hailstones[1][5] * t2 == e + f * t2)
    solver.add(hailstones[2][0] + hailstones[2][3] * t3 == a + b * t3)
    solver.add(hailstones[2][1] + hailstones[2][4] * t3 == c + d * t3)
    solver.add(hailstones[2][2] + hailstones[2][5] * t3 == e + f * t3)
    solver.add(answer == a + c + e)
    if solver.check() != sat: return None
    return solver.model()[answer]

if __name__ == "__main__":
    print(f"The answer is {main()}")
