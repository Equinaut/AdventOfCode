allPoints = dict()

lines = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        points = line.split(" -> ")
        point1 = (int(points[0].split(",")[0]), int(points[0].split(",")[1]))
        point2 = (int(points[1].split(",")[0]), int(points[1].split(",")[1]))
        if (point1[0] == point2[0] or point1[1] == point2[1] or (abs(point2[0] - point1[0]) == abs(point2[1] - point1[1]))):
            lines.append((point1, point2))

for line in lines:
    xDirection = 0
    yDirection = 0
    if line[1][1] < line[0][1]: yDirection = -1
    elif line[1][1] > line[0][1]: yDirection = 1
    if line[1][0] < line[0][0]: xDirection = -1
    elif line[1][0] > line[0][0]: xDirection = 1
    
    length = max(abs(line[0][1] - line[1][1]), abs(line[1][0] - line[0][0]))
    
    for i in range(0, length + 1):
        x = line[0][0] + xDirection * i
        y = line[0][1] + yDirection * i

        point = f"{str(x)}-{str(y)}"
        if point not in allPoints:
            allPoints[point] = 1
        else:
            allPoints[point] += 1

print(f"The answer is {sum([1 if count > 1 else 0 for count in allPoints.values()])}")
