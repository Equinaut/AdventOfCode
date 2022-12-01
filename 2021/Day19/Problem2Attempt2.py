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
    while coordinatesLength < len(lines) and lines[coordinatesLength]!="\n": coordinatesLength+=1
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

transformationsNoTranslations = {}

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
                                    beacon2[orientation[2]] * flips[2] * -1
                                )

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

                                    print(f"Intersection: {scanner0}, {scanner1}, {flips},{orientation}, \t{len(intersection)}, \t{scanner1Scanner0Offset}")
                                    transformationsNoTranslations[scanner0, scanner1] = (flips, orientation)

                                    transform(*transformations[-1])


for scanner, coords in coordsRelativeTo.items():
    print(scanner.name, len(coords))
    print(coords)
    print("\n\n")

scannerLocations = {}

transformationsNoTranslations[scanners[0], scanners[0]] = ((1, 1, 1), (0, 1, 2))

print("Generate new translations")
for (destination1, origin1), translation1 in transformationsNoTranslations.items():
    for (destination2, origin2), translation2 in transformationsNoTranslations.items():
        if origin1 != destination2: continue
        if destination1 == origin2: continue
        newTranslation = (
            (
                translation1[0][translation1[1][0]] * translation2[0][0],
                translation1[0][translation1[1][1]] * translation2[0][1],
                translation1[0][translation1[1][2]] * translation2[0][2]
            ),
            (
                translation1[1][translation2[1][0]], 
                translation1[1][translation2[1][1]], 
                translation1[1][translation2[1][2]]
            )
        )
        print(destination1, origin2, translation1, translation2, newTranslation)

print("Transformation no translation")
for locations, translation in transformationsNoTranslations.items():
    print(locations, translation)
print("\n\n")

for scanner in scanners:
    for scanner1 in scanners:
        if scanner == scanner1: continue

        if (scanners[0], scanner) not in transformationsNoTranslations: continue
        if (scanners[0], scanner1) not in transformationsNoTranslations: continue

        flips1, orientation1 = transformationsNoTranslations[scanners[0], scanner]
        flips2, orientation2 = transformationsNoTranslations[scanners[0], scanner1]
        for coords in scanner.getCoordinates(flips = flips1, axis = orientation1):
            for coords2 in scanner.getCoordinates(flips = flips1, axis = orientation1):

                if coords == coords2: continue

                for coords3 in scanner1.getCoordinates(flips = flips2, axis = orientation2):
                    for coords4 in scanner1.getCoordinates(flips = flips2, axis = orientation2):
                        if coords3 == coords4: continue

                        difference1 = [i-j for i,j in zip(coords, coords2)]
                        difference2 = [i-j for i,j in zip(coords3, coords4)]

                        if difference1 == difference2:
                            print(scanner1, flips, orientation, [i-j for i,j in zip(coords, coords3)])
                            scannerLocations[scanner, scanner1] = [i-j for i,j in zip(coords, coords3)]

for scanners, relativeLocation in scannerLocations.items():
    print(scanners, relativeLocation)