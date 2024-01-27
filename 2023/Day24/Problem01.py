import numpy as np

MINPOS = 7
MAXPOS = 27

MINPOS = 200000000000000
MAXPOS = 400000000000000

def main():
    ans = 0

    hailstones = list()
    with open("input.txt") as file:
        for line in file:
            x1, y1, z1, xv, yv, zv = list(map(int, line.replace("@", ",").split(",")))
            hailstones.append((x1, y1, xv, yv))
    
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[:i]:
            if linesIntersects(h1, h2): ans += 1
    return ans

def linesIntersects(line1, line2):
    x1, y1, xt1, yt1 = line1
    x2, y2, xt2, yt2 = line2
    e1 = np.array([[-xt1, xt2], [-yt1, yt2]])
    e2 = np.array([x1 - x2, y1 - y2])        
    
    try:
        solution = np.linalg.solve(e1, e2)
        if min(solution) < 0: return False
        intersectX, intersectY = x1 + xt1 * solution[0], y1 + yt1 * solution[0]
        if intersectX < MINPOS or intersectX > MAXPOS: return False
        if intersectY < MINPOS or intersectY > MAXPOS: return False
        return True
    except np.linalg.LinAlgError:
        return False

if __name__ == "__main__":
    print(f"The answer is {main()}")