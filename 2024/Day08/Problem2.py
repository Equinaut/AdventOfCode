import math

def main():
    anntenas = dict()
    with open("input.txt") as file:
        lines = file.readlines()
        width, height = len(lines[0]) - 1, len(lines)
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                if c != "." and c != "#":
                    if c not in anntenas: anntenas[c] = set()
                    anntenas[c].add((x, y))

    locations = set()
    for c in anntenas:
        for x1, y1 in anntenas[c]:
            for x2, y2 in anntenas[c]:
                if (x1, y1) == (x2, y2): continue
                xOff = x1 - x2
                yOff = y1 - y2
                xOff = xOff // math.gcd(xOff, yOff)
                yOff = yOff // math.gcd(xOff, yOff)
                nextLocation = (x1, y1)
                while nextLocation[0] >= 0 and nextLocation[1] >= 0 and nextLocation[0] < width and nextLocation[1] < height:
                    locations.add(nextLocation)
                    nextLocation = (nextLocation[0] + xOff, nextLocation[1] + yOff)
                    
    return len(locations)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")