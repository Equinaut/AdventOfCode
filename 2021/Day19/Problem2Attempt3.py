import itertools

scanners = []
class Scanner:
    def __init__(self, nameTemp, positions):
        self.beacons = set(positions)
        self.name = nameTemp[:-1]

    def __repr__(self):
        return f"Scanner({self.name})"

    def getCoords(self, flips = (1, 1, 1), axis = (0, 1, 2), offsetFromScanner0 = (0, 0, 0)):
        coordinatesChanged = []
        for c in self.beacons:
            coordinatesChanged.append(
                (c[axis[0]] * flips[0] + offsetFromScanner0[0],
                c[axis[1]] * flips[1] + offsetFromScanner0[1], 
                c[axis[2]] * flips[2] + offsetFromScanner0[2])
                )
        return coordinatesChanged

def getCoords(scanner, flips = (1, 1, 1), axis = (0, 1, 2), offsetFromScanner0 = (0, 0, 0)):
    coordinatesChanged = []
    for c in coordsRelativeTo[scanner]:
        coordinatesChanged.append(
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

                                scanner0Normal = scanner0.getCoords()
                                scanner0Offsets = scanner0.getCoords(offsetFromScanner0 = scanner0Scanner0Offset)
                                scanner1Normal = scanner1.getCoords()
                                scanner1Offsets = scanner1.getCoords(flips, orientation, scanner1Scanner0Offset)

                                scanner1Oriented = scanner1.getCoords(flips, orientation)

                                intersection = set()
                                relativeToS0 = []
                                relativeToS1 = []

                                for offset, normal in zip(scanner0Offsets, scanner0Normal):
                                    if offset in scanner1Offsets:
                                        intersection.add(offset)
                                        relativeToS0.append(normal)
                                        relativeToS1.append(scanner1Oriented[scanner1Offsets.index(offset)])

                                if len(intersection) >= 12:
                                    transformations.append((scanner0, scanner1, scanner0Scanner0Offset, scanner1Scanner0Offset, flips, orientation))

                                    print(f"All {scanner1.name} coords relative to {scanner0.name}")
                                    print(f"{flips},{orientation}, \t{len(intersection)}, \t{scanner1Scanner0Offset}")
                                    print(relativeToS0)
                                    print(relativeToS1)
                                    print()
