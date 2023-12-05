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
        seeds = [createSeed(int(i)) for i in file.readline()[7:-1].split(" ")]
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

    for seed in seeds:
        convertSeed(seed, convertions)
    

    return min(seeds, key = lambda a: a["location"])["location"]

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
    