import itertools

scanners = []
class Scanner:
    def __init__(self, nameTemp, positions):
        self.beacons = set(positions)
        self.name = nameTemp[:-1]

    def __repr__(self):
        return f"Scanner({self.name})"

    def getCoordinates(self, flips = (1, 1, 1), axis = (0, 1, 2), offsetFromScanner0 = (0, 0, 0)):
        coordinatesChanged = set()
        for c in self.beacons:
            coordinatesChanged.add(
                (c[axis[0]] * flips[0] + offsetFromScanner0[0],
                c[axis[1]] * flips[1] + offsetFromScanner0[1], 
                c[axis[2]] * flips[2] + offsetFromScanner0[2])
                )
        return coordinatesChanged

def getCoords(scanner, flips = (1, 1, 1), axis = (0, 1, 2), offsetFromScanner0 = (0, 0, 0)):
    coordinatesChanged = set()
    for c in coordsRelativeTo[scanner]:
        coordinatesChanged.add(
                (c[axis[0]] * flips[0] + offsetFromScanner0[0],
                c[axis[1]] * flips[1] + offsetFromScanner0[1], 
                c[axis[2]] * flips[2] + offsetFromScanner0[2])
                )
    return coordinatesChanged

with open("inputSmall.txt", "r") as file:
    lines = file.readlines()

while len(lines) > 0:
    lines.pop(0)
    coordinates = []
    coordinatesLength = 0
    while coordinatesLength < len(lines) and lines[coordinatesLength] != "\n":
        coordinatesLength += 1
    name = lines[0]
    for line in lines[1:coordinatesLength]:
        coordinates.append(tuple(int(i) for i in line[:-1].split(",")))
    scanners.append(Scanner(name, [c for c in coordinates]))
    lines = lines[coordinatesLength:]


allCoords = set()
for coords in scanners[0].beacons:
    allCoords.add(coords)

transformations = []

coordsRelativeTo = {}

def transform(scanner0, scanner1, scanner0Scanner0Offset, scanner1Scanner0Offset, flips, orientation):
    for coord in getCoords(scanner1, flips, orientation, scanner1Scanner0Offset):
        changedCoord = (
            coord[0] - scanner0Scanner0Offset[0],
            coord[1] - scanner0Scanner0Offset[1],
            coord[2] - scanner0Scanner0Offset[2]
            )
        #print(changedCoord, end=", ")
        if scanner0 not in coordsRelativeTo: coordsRelativeTo[scanner0]=set()

        coordsRelativeTo[scanner0].add(changedCoord)

        if scanner0.name == "--- scanner 0 ---":
            allCoords.add(changedCoord)


for scanner in scanners:
    if scanner not in coordsRelativeTo: coordsRelativeTo[scanner] = set()
    for beacon in scanner.beacons: coordsRelativeTo[scanner].add(beacon)

for scanner0 in scanners:
    for scanner1 in scanners:
        if scanner0.name==scanner1.name: continue
        
        print(scanner0.name, scanner1.name)
        for orientation in itertools.permutations((0, 1, 2)):
            for flips0 in range(-1, 2, 2):
                for flips1 in range(-1, 2, 2):
                    for flips2 in range(-1, 2, 2):
                        flips = (flips0, flips1, flips2)
                        for beacon in scanner0.beacons:
                            for beacon2 in scanner1.beacons:
                                scanner0Scanner0Offset = (beacon[0] * -1, beacon[1] * -1, beacon[2] * -1)
                                scanner1Scanner0Offset = (
                                    beacon2[orientation[0]] * flips[0] * -1, 
                                    beacon2[orientation[1]] * flips[1] * -1, 
                                    beacon2[orientation[2]] * flips[2] * -1)

                                scanner0Offsets = getCoords(scanner0, offsetFromScanner0 = scanner0Scanner0Offset)
                                scanner1Offsets = getCoords(scanner1, flips, orientation, scanner1Scanner0Offset)
                                intersection = scanner0Offsets.intersection(scanner1Offsets)

                                actualIntersection = []
                                for coords in intersection:
                                    actualIntersection.append(
                                        (coords[0] - scanner0Scanner0Offset[0], 
                                        coords[1] - scanner0Scanner0Offset[1], 
                                        coords[2] - scanner0Scanner0Offset[2]))
                                    
                                if len(intersection) >= 12:
                                    transformations.append((scanner0, scanner1, scanner0Scanner0Offset, scanner1Scanner0Offset, flips, orientation))

                                    print(f"{actualIntersection}, \t,  {flips},{orientation}, \t{len(intersection)}, \t{scanner1Scanner0Offset}")
                                    print()
                                    print(f"All {scanner1.name} coords relative to {scanner0.name}")
                                    
                                    #transform(*transformations[-1])
                                    print()

for scanner, coords in coordsRelativeTo.items():
    print(scanner.name, len(coords))
    print(coords)
    print("\n\n")


print("\n\n\n")

#Scanner 1 relative to scanner 0
print("\n".join([str(i) for i in transformations]))
print(allCoords)
print()
for i in range(0, len(scanners)):
    for transformation in transformations:
        transform(*transformation)

for scanner, coords in coordsRelativeTo.items():
    print(scanner, len(coords))

for transformation in transformations: print(transformation)


print("\n\nOrientation transformations from scanner 0\n") #Calculating transformations to orient all sets of scanners, the same orientation as scanner 0
orientationAxisTransformationsFromScanner0 = dict()

for i in range(0, 10):
    newTransformations = set()
    for transformation in transformations:
        #if transformation[0]!= scanners[0]: continue
        for transformation2 in transformations:
            if transformation[1] != transformation2[0]: continue
            #print("Starting a double transformation", i)
            #print(transformation)
            #print(transformation2)
            newFlips = (transformation[4][0] * transformation2[4][0], transformation[4][1] * transformation2[4][1], transformation[4][2] * transformation2[4][2])
            newOrientation = (transformation[5][transformation2[5][0]], transformation[5][transformation2[5][1]], transformation[5][transformation2[5][2]])

            newTransformation = (transformation[0], transformation2[1], (0, 0, 0), (0, 0, 0), newFlips, newOrientation)
            newTransformations.add(newTransformation)
            
            #print("\n")
    for transformation in newTransformations:
        transformations.append(transformation)

print("\n\n")

for transformation in transformations:
    if transformation[0] == scanners[0]:
        orientationAxisTransformationsFromScanner0[transformation[0], transformation[1]] = transformation

for key, transformation in orientationAxisTransformationsFromScanner0.items():
    print(key, transformation)

print("\n\nAll orientation transformations:\n ")
print(orientationAxisTransformationsFromScanner0)
for key, value in orientationAxisTransformationsFromScanner0.items():
    print(key, value)
print()
scannerPositions = {}
print(len(transformations))
print("\n\n\nScanner positions\n\n")
destinations = set()

transformationsFrom0 = set()
for transformation in transformations:
    if transformation[0] == scanners[0]:
        transformationsFrom0.add(transformation)

for scanner2 in scanners:
    print(scanner2)
    for transformation in transformationsFrom0:
        
        if transformation[1] != scanner2: continue
        for coords in scanner.beacons:
            for coords2 in scanner.beacons:
                if coords == coords2: continue
                for coords3 in scanner2.getCoordinates(transformation[4], transformation[5]):
                    for coords4 in scanner2.getCoordinates(transformation[4], transformation[5]):
                        if coords3 == coords4: continue

                        difference = [i-j for i, j in zip(coords, coords2)]
                        difference2 = [i-j for i, j in zip(coords3, coords4)]
                        if difference == difference2:
                            
                            print(scanner, scanner2, coords, coords2, coords3, coords4, difference, difference2)
                            scannerPositions[scanner2] = [i-j for i, j in zip(coords, coords3)]
                            #print(f"{scanner2.name} is at {[i-j for i, j in zip(coords, coords3)]}")

print("\n\n\nFinal scanner positions\n\n")
for scanner, position in scannerPositions.items():
    print(scanner, position)


print()
print(f"The answer is {len(coordsRelativeTo[scanners[0]])}")