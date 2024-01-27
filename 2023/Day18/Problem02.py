def main():
    currentX, currentY = 0, 0

    xPositions = list()
    yPositions = list()

    lines = []

    positions = [(0, 0)]
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            direction, distance, _ = line.split(" ")
            code = line.split(" ")[2][2:]
            direction = code[5]
            distance = int(code[:5], base=16)
            if direction == "0": #R
                newX = currentX + distance
                newY = currentY
            if direction == "1": #D
                newY = currentY + distance
                newX = currentX
            if direction == "2": #L
                newX = currentX - distance
                newY = currentY
            if direction == "3": #U
                newY = currentY - distance
                newX = currentX
            positions.append((newX, newY))
            currentX = newX
            currentY = newY

    xPositions = set()
    yPositions = set()
    for x, y in positions:
        xPositions.add(x)
        xPositions.add(x + 1)
        yPositions.add(y)
        yPositions.add(y + 1)

    xPositions = list(sorted(xPositions))
    yPositions = list(sorted(yPositions))

    digPositions = set()
    lastX, lastY = positions[0]

    for x, y in positions:
        x2 = xPositions.index(x)
        y2 = yPositions.index(y)

        for x3 in range(x2, lastX + 1): digPositions.add((x3, lastY))
        for x3 in range(x2, lastX - 1, - 1): digPositions.add((x3, lastY))
        for y3 in range(y2, lastY + 1): digPositions.add((lastX, y3))
        for y3 in range(y2, lastY - 1, - 1): digPositions.add((lastX, y3))

        lastX, lastY = x2, y2
    
    notPositions = set()
    queue = []
    for x in range(-1, len(xPositions) + 1):
        queue.append((x, -1))
        queue.append((x, len(yPositions) + 1))
    
    for y in range(-1, len(yPositions) + 1):
        queue.append((-1, y))
        queue.append((len(xPositions) + 1, y))

    while queue:
        x, y = queue.pop(0)
        if (x, y) in digPositions: continue
        if (x, y) in notPositions: continue
        notPositions.add((x, y))
        if x < -1 or y < -1: continue
        if x > len(xPositions) + 1 or y > len(yPositions) + 1: continue
        queue.append((x - 1, y))
        queue.append((x + 1, y))
        queue.append((x, y - 1))
        queue.append((x, y + 1))

    if (0, 0) not in notPositions:
        topPos = 0
        leftPos = 1
        while (topPos, 0) not in notPositions: 
            notPositions.add((topPos, 0))
            topPos += 1
        while (0, leftPos) not in notPositions:
            notPositions.add((0, leftPos))
            leftPos += 1

    ans = 0
    for y2 in range(0, len(yPositions) - 1):
        for x2 in range(0, len(xPositions) - 1):
            xWidth = abs(xPositions[x2 + 1] - xPositions[x2])
            yHeight = abs(yPositions[y2 + 1] - yPositions[y2])
            if (x2, y2) not in notPositions:
                ans += xWidth * yHeight
    return ans

def printGrid(xPositions, yPositions, notPositions):
    for y2 in range(0, len(yPositions)):
        for x2 in range(0, len(xPositions)):
            if (x2, y2) not in notPositions:
                print("🟨", end="")
            else:
                print("⬜", end="")
        print()

if __name__ == "__main__":
    print(f"The answer is {main()}")