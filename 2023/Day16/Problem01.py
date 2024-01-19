RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4

def main():
    ans = 0
    beams = {(0, 0, RIGHT)}
    with open("input.txt") as file:
        contents = [line[:-1] for line in file.readlines()]

    visited = set()

    visitedNew = True
    i  = 0
    while visitedNew:
        visitedNew = i < 2000
        i += 1

        newBeams = set()
        for beam in beams:
            x, y, direction = beam


            if x < 0 or y < 0 or x >= len(contents[0]) or y >= len(contents): continue
            visited.add((x, y))
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

    for y in range(0, len(contents)):
        for x in range(0, len(contents)):
            if (x, y) in visited: 
                ans += 1
                print("#", end="")
            else: print(".", end="")
        print()


    return ans

def moveBeam(x, y, direction):
    if direction == RIGHT: return (x + 1, y, RIGHT)
    if direction == UP: return (x, y - 1, UP)
    if direction == LEFT: return (x - 1, y, LEFT)
    if direction == DOWN: return (x, y + 1, DOWN)

if __name__ == "__main__":
    print(f"The answer is {main()}")