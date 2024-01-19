RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4

def main():
    with open("input.txt") as file:
        contents = [line[:-1] for line in file.readlines()]

    maxAns = 0
    for x in range(0, len(contents[0])):
        print("X:", x)
        a = countVisited(contents, (x, 0, DOWN))
        b = countVisited(contents, (x, len(contents) - 1, UP))
        maxAns = max(maxAns, a, b)

    for y in range(0, len(contents)):
        print("Y:", y)
        a = countVisited(contents, (0, y, RIGHT))
        b = countVisited(contents, (len(contents[0]) - 1, y, LEFT))
        maxAns = max(maxAns, a, b)

    return maxAns

def countVisited(contents, start):
    beams = {start}
    visited = set()
    visitedNew = True
    i  = 0
    while visitedNew:
        visitedNew = False
        i += 1
        newBeams = set()
        for beam in beams:
            x, y, direction = beam
            if x < 0 or y < 0 or x >= len(contents[0]) or y >= len(contents): continue
            if (x, y, direction) not in visited: visitedNew = True
            visited.add((x, y, direction))
            m = contents[y][x]
            if m == ".":
                newBeams.add(moveBeam(*beam))
            elif m == "|":
                if direction == RIGHT or direction == LEFT:
                    newBeams.add((x, y - 1, UP))
                    newBeams.add((x, y + 1, DOWN))
                if direction == UP or direction == DOWN:
                    newBeams.add(moveBeam(*beam))
            elif m == "-":
                if direction == UP or direction == DOWN:
                    newBeams.add((x + 1, y, RIGHT))
                    newBeams.add((x - 1, y, LEFT))
                if direction == LEFT or direction == RIGHT:
                    newBeams.add(moveBeam(*beam))
            else:
                if m == "/":
                    if direction == RIGHT: newBeams.add((x, y - 1, UP))
                    if direction == UP: newBeams.add((x + 1, y, RIGHT))
                    if direction == LEFT: newBeams.add((x, y + 1, DOWN))
                    if direction == DOWN: newBeams.add((x - 1, y, LEFT))

                elif m == "\\":
                    if direction == RIGHT: newBeams.add((x, y + 1, DOWN))
                    if direction == UP: newBeams.add((x - 1, y, LEFT))
                    if direction == LEFT: newBeams.add((x, y - 1, UP))
                    if direction == DOWN: newBeams.add((x + 1, y, RIGHT))
        beams = newBeams
    return len(set((x,y) for (x, y, _) in visited))

def moveBeam(x, y, direction):
    if direction == RIGHT: return (x + 1, y, RIGHT)
    if direction == UP: return (x, y - 1, UP)
    if direction == LEFT: return (x - 1, y, LEFT)
    if direction == DOWN: return (x, y + 1, DOWN)

if __name__ == "__main__":
    print(f"The answer is {main()}")