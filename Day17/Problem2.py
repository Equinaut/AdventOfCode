with open("input.txt", "r") as file:
    line = file.readline()[:-1]
    coords = line.split("target area: ")[1]
    xCoords, yCoords = (c[2:] for c in coords.split(", "))
    xMin = int(xCoords.split("..")[0])
    xMax = int(xCoords.split("..")[1])
    yMin = int(yCoords.split("..")[0])
    yMax = int(yCoords.split("..")[1])

def hits(xChange, yChange):
    x = y = 0
    while True:
        x += xChange
        y += yChange
        if xChange > 0: xChange-=1
        elif xChange < 0: xChange+=1
        yChange-=1

        if x >= xMin and x <= xMax and y>=yMin and y<=yMax: return True, None

        if y < yMin and yChange < 0: 
            return None, 0
            if x > xMax: return None, 1
            elif x < xMin: return None, -1
            else: return None, 0
        if x > xMax and xChange < 0: return None, 1

amountOfHits = 0
   
y=0
while True:
    x = 0
    while True:
        h = hits(x, y)
        h2 = hits(x + 1, y)
        
        if h[0]: 
            amountOfHits+=1
            print(x, y, h, h2, amountOfHits)

        #if h[0] is not None and h2[0] is None: break
        if h[0] is None and h2[0] is None and h[1] != h2[1]: break

        if x > xMax: break
        x+=1

    if y > 0: y *= -1
    else: y = y*-1 + 1
    print(y, amountOfHits)

    if y > 10000: break
