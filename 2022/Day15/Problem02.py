sensors = []
calcDistance = lambda x1, y1, x2, y2: abs(x2 - x1) + abs(y2 - y1)

def emptyRangeRow(beacon, distance, row):
    rowDiff = abs(beacon[1] - row)
    if rowDiff > distance: return None
    return (beacon[0] - distance + rowDiff, beacon[0] + distance - rowDiff)

def isFull(row):
    emptyRanges = [emptyRange for beacon, distance in sensors if ((emptyRange := emptyRangeRow(beacon, distance, row)) is not None)]

    if len(emptyRanges) == 0: return False

    emptyRanges.sort(key = lambda currentRange: currentRange[0])

    if emptyRanges[0][0] > 0: return False
    maxX = emptyRanges[0][1]

    while len(emptyRanges):      
        currentRange = emptyRanges.pop(0)
        if len(emptyRanges) and emptyRanges[0][0] <= maxX + 1 and emptyRanges[0][1] > currentRange[1]: 
            continue
        if currentRange[0] <= maxX + 1 and currentRange[1] > maxX: maxX = currentRange[1]
        if maxX >= area: return True

    return maxX >= area

def findGap(row):
    emptyRanges = [emptyRange for beacon, distance in sensors if ((emptyRange := emptyRangeRow(beacon, distance, row)) is not None)]
    for x in range(0, area + 1):
        inAnyRange = False
        for currentRange in emptyRanges:
            if x >= currentRange[0] and x <= currentRange[1]:
                inAnyRange = True
                break
        if not inAnyRange: return x
    return None

calculateTuningFrequency = lambda x, y: x * 4_000_000 + y

area = 4_000_000
with open("input.txt") as file:
    for line in file.readlines():
        beacon = ([[int(c) for c in coords.split(", y=")] for coords in line[12:-1].split(": closest beacon is at x=")])
        sensors.append((beacon[0], calcDistance(*beacon[0], *beacon[1])))
sensors.sort(key = lambda sensor : sensor[0][0])

answer = None
for row in range(area):
    if not isFull(row): 
        answer = calculateTuningFrequency(findGap(row), row)
        break

print(f"The answer is {answer}")