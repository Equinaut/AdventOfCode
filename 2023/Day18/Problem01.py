def main():
    ans = 0
    minX = maxX = minY = maxY = 0
    currentX, currentY = 0, 0

    digPositions = set()
    with open("input.txt") as file:
        for line in file:
            direction, distance, _ = line.split(" ")
            if direction == "R":
                newX = currentX + int(distance)
                newY = currentY
            if direction == "L":
                newX = currentX - int(distance)
                newY = currentY
            if direction == "U":
                newX = currentX
                newY = currentY - int(distance)
            if direction == "D":
                newX = currentX
                newY = currentY + int(distance)
            if newX < minX: minX = newX
            if newX > maxX: maxX = newX
            if newY < minY: minY = newY
            if newY > maxY: maxY = newY
            for x in range(currentX, newX + 1): digPositions.add((x, currentY))
            for x in range(currentX, newX - 1, - 1): digPositions.add((x, currentY))
            for y in range(currentY, newY): digPositions.add((currentX, y))
            for y in range(currentY, newY - 1, - 1): digPositions.add((currentX, y))
            currentX = newX
            currentY = newY

    notDigPositions = set()
    minX -= 1
    minY -= 1
    maxY += 1
    maxX += 1

    queue = [(minX, minY)]

    while queue:
        x, y = queue.pop(0)
        if (x, y) in digPositions: continue
        if (x, y) in notDigPositions: continue
        notDigPositions.add((x, y))
        if x < minX: continue
        if x > maxX: continue
        if y < minY: continue
        if y > maxY: continue
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

    ans = 0
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            if (x, y) not in notDigPositions: ans += 1
    return ans

def printGrid(digPositions, minX, maxX, minY, maxY):
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in digPositions: print("#", end="")
            else: print(".", end="")
        print()

if __name__ == "__main__":
    print(f"The answer is {main()}")