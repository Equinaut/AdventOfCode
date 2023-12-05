import copy

def createSeed(seedNum):
    return {
        "seed": seedNum,
        "fertilizer": None,
        "soil": None,
        "water": None,
        "light": None,
        "temperature": None,
        "humidity": None,
        "location": None
    }

def main():
    ans = 0
    with open("input.txt") as file:
        seedsLine = [int(i) for i in file.readline()[7:-1].split(" ")]
        seedRanges = []
        for i in range(0, len(seedsLine), 2):
            seedRanges.append((seedsLine[i], seedsLine[i] + seedsLine[i + 1]))

        file.readline()
        lines = file.readlines()
    lines.append("\n")

    currentType = None
    currentVals = []
    convertions = []
        
    for line in lines:
        if line == "\n":
            fromCat = currentType.split("-")[0]
            toCat = currentType.split(" ")[0].split("-")[2]
            convertions.append((fromCat, toCat, copy.copy(currentVals)))
            currentType = None
            currentVals = []

        elif currentType is None:
            currentType = line[:-1]
        else:
            currentVals.append([int(i) for i in line[:-1].split(" ")])

    bounds = set()
    for i in range(6, -1 , -1):
        newBounds = set()
        for bound in bounds:
            for convertion in convertions[i][2]:
                if bound >= convertion[0] and (bound <= convertion[0] + convertion[2] or bound <= convertion[1] + convertion[2]):
                    newBounds.add(bound + convertion[1] - convertion[0])
        bounds |= newBounds

        for bound in convertions[i][2]:
            bounds.add(bound[1])
            bounds.add(bound[1] + bound[2])
    
    ans = None
    for bound in bounds:
        if not any(bound >= r[0] and bound < r[1] for r in seedRanges): continue
        s = createSeed(bound)
        convertSeed(s, convertions)
        if ans is None or s["location"] < ans:
            ans = s["location"]
    return ans

def convertSeed(seed, convertions):
    for (fromCat, toCat, currentVals) in convertions:
        for (destStart, sourceStart, r) in currentVals:
            if seed[fromCat] is None: continue
            if seed[fromCat] >= sourceStart and seed[fromCat] < sourceStart + r:
                rangeVal = seed[fromCat] - sourceStart
                destVal = destStart + rangeVal
                seed[toCat] = destVal
        if seed[toCat] is None: seed[toCat] = seed[fromCat]
    return seed

if __name__ == "__main__":
    print(f"The answer is {main()}")
    