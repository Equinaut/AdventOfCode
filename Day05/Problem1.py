allPoints = dict()

lines = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        points = line.split(" -> ")
        point1 = (int(points[0].split(",")[0]), int(points[0].split(",")[1]))
        point2 = (int(points[1].split(",")[0]), int(points[1].split(",")[1]))
        if (point1[0] == point2[0] or point1[1] == point2[1]):
            lines.append((point1, point2))

for line in lines:
    minX = min(line[0][0], line[1][0])
    maxX = max(line[0][0], line[1][0])

    minY = min(line[0][1], line[1][1])
    maxY = max(line[0][1], line[1][1])
    
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            point = f"{str(x)}-{str(y)}"
            if point not in allPoints:
                allPoints[point] = 1
            else:
                allPoints[point] += 1

print(f"The answer is {sum([1 if count > 1 else 0 for count in allPoints.values()])}")