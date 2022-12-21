sensors = []
calculateDistance = lambda x1, y1, x2, y2: abs(x2 - x1) + abs(y2 - y1)

def getEmptyRange(beacon, sensor, row):
    distance = calculateDistance(*beacon, *sensor)
    rowDiff = abs(beacon[1] - row)
    if rowDiff > distance: return None
    return (beacon[0] - distance + rowDiff, beacon[0] + distance - rowDiff)

row = 2_000_000
with open("input.txt") as file:
    for line in file.readlines():
        beacon = [list(map(int, coords.split(", y="))) for coords in line[12:-1].split(": closest beacon is at x=")]
        sensors.append((beacon[0], beacon[1]))

emptyRanges = [emptyRange for beacon in sensors if (emptyRange := getEmptyRange(beacon[0], beacon[1], row)) is not None]
emptyRanges.sort(key = lambda a : a[0])

answer = 0
for currentRange in emptyRanges:
    while len(emptyRanges) and emptyRanges[0][0] >= currentRange[0] and emptyRanges[0][0] <= currentRange[1]:
        currentRange = (currentRange[0], max(currentRange[1], emptyRanges.pop(0)[1]))
    answer += currentRange[1] - currentRange[0]

print(f"The answer is {answer}")