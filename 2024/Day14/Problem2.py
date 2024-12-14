WIDTH = 101
HEIGHT = 103

def stepRobots(robots):
    newRobots = []
    for (xPos, yPos), (xVel, yVel) in robots:
        newXPos = xPos + xVel
        newYPos = yPos + yVel

        if newXPos < 0: newXPos = WIDTH + newXPos
        if newYPos < 0: newYPos = HEIGHT + newYPos

        if newXPos >= WIDTH: newXPos -= WIDTH
        if newYPos >= HEIGHT: newYPos -= HEIGHT

        newRobots.append(((newXPos, newYPos), (xVel, yVel)))
    return newRobots

def getGrid(robots):
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for ((x, y), _) in robots:
        grid[y][x] += 1
    return grid

def printGrid(robots):
    grid = getGrid(robots)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            if grid[y][x] == 0: print(f"⬛", end="")
            else: print(f"🟩", end="")
        print()

def checkForLine(robots):
    grid = getGrid(robots)
    minLength = 15
    for ((x, y), _) in robots:
        if all(x + i < WIDTH and grid[y][x + i] > 0 for i in range(minLength)):
            return True
    return False

def main():
    robots = []
    with open("input.txt") as file:
        for line in file:
            robot = tuple((tuple(int(x) for x in point[2:].split(",")) for point in line.split(" ")))
            robots.append(robot)
    i = 1
    while True: 
        robots = stepRobots(robots)
        if checkForLine(robots):
            printGrid(robots)
            return i
        i += 1

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")