with open("input.txt", "r") as file:
    line = file.readline()[:-1]
    coords = line.split("target area: ")[1]
    xCoords, yCoords = (c[2:] for c in coords.split(", "))
    xMin = int(xCoords.split("..")[0])
    xMax = int(xCoords.split("..")[1])
    yMin = int(yCoords.split("..")[0])
    yMax = int(yCoords.split("..")[1])

def hits(xChange, yChange):
    x = y = peakY = previousY = 0
    while True:
        previousY = y
        x += xChange
        y += yChange
        if xChange > 0: xChange-=1
        elif xChange < 0: xChange+=1
        yChange-=1
        if y > peakY: peakY = y

        if x >= xMin and x <= xMax and y>=yMin and y<=yMax: return True, peakY
        if y < yMin and yChange < 0: 
            if x > xMax: return None, 1
            if x < xMin: return None, -1
            if previousY > yMax and y < yMin: return None, 0
        if x > xMax and xChange < 0: return None, 1


overallPeakY = 0 
peakYForY = 0   
y=4
while True:
    x = 0
    peakY = 0 
    while True:
        h = hits(x, y)
        h2 = hits(x + 1, y)
        
        if h[0] and h[1] > peakY: 
            peakY = h[1]
            print(y, x, h, h2, overallPeakY, peakYForY)

        if h[0] is not None and h2[0] is None: break
        if h[0] is None and h2[0] is None and h[1] != h2[1]: break

        if x > xMax: break
        x+=1
    if peakY > overallPeakY: 
        overallPeakY = peakY
        peakYForY = y

    y+=1
    if y > 10000: break
