def main():
    points = []
    with open("input.txt") as file:
        for line in file:
            points.append(tuple(map(int, line[:-1].split(","))))
    
    ans = 0
    for i, (x1, y1) in enumerate(points):
        for (x2, y2) in points[:i]:
            ans = max(ans, (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1))
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
