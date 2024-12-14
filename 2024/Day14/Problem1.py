WIDTH = 101
HEIGHT = 103

def stepRobots(robots):
    newRobots = []
    for (xPos, yPos), (xVel, yVel) in robots:
        newXPos = (xPos + xVel) % WIDTH
        newYPos = (yPos + yVel) % HEIGHT
        newRobots.append(((newXPos, newYPos), (xVel, yVel)))
    return newRobots

def safetyFactor(robots):
    middleX = WIDTH // 2
    middleY = HEIGHT // 2
    topLeft = topRight = botLeft = botRight = 0
    for ((x, y), _) in robots:
        if x < middleX and y < middleY: topLeft += 1
        elif x > middleX and y < middleY: topRight += 1
        elif x < middleX and y > middleY: botLeft += 1
        elif x > middleX and y > middleY: botRight += 1
    return topLeft * topRight * botLeft * botRight

def main():
    robots = []
    with open("input.txt") as file:
        for line in file:
            robot = tuple((tuple(int(x) for x in point[2:].split(",")) for point in line.split(" ")))
            robots.append(robot)
    for _ in range(100): robots = stepRobots(robots)
    return safetyFactor(robots)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")