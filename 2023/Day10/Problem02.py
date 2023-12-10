def main():
    pipeMapOld = []
    with open("input.txt") as file:
        for y, line in enumerate(file):
            pipeMapOld.append([])
            for x, p in enumerate(line[:-1]):
                if p == "S":
                    start = (x, y)
                    pipeMapOld[-1].append(None)
                else:
                    pipeMapOld[-1].append({
                        "w": p == "-" or p == "7" or p == "J",
                        "e": p == "-" or p == "L" or p == "F",
                        "n": p == "|" or p == "L" or p == "J",
                        "s": p == "|" or p == "7" or p == "F",
                    })
    
    width = len(pipeMapOld[0])
    height = len(pipeMapOld)
    pipeMap = []
    for y in range(height * 2):
        pipeMap.append([])
        for x in range(0, width * 2):
            if x % 2 == 0 and y % 2 == 0:
                pipeMap[-1].append(pipeMapOld[y // 2][x // 2])
            else:
                pipeMap[-1].append({
                    "w": False,
                    "e": False,
                    "n": False,
                    "s": False,
                })
    
    start = (start[0] * 2, start[1] * 2)
    pipeMap[start[1]][start[0]] = {
        "w": pipeMap[start[1]][start[0] - 2]["e"],
        "e": pipeMap[start[1]][start[0] + 2]["w"],
        "n": pipeMap[start[1] - 2][start[0]]["s"],
        "s": pipeMap[start[1] + 2][start[0]]["n"],
    }

    for y in range(0, height):
        for x in range(0, width):
            p = pipeMap[y * 2][x* 2]
            if p is None: continue
            if p["e"]: pipeMap[y * 2][x * 2 + 1]["w"] = True
            if p["w"]: pipeMap[y * 2][x * 2 - 1]["e"] = True
            if y > 0 and y < height and p["n"]: pipeMap[y * 2 - 1][x * 2]["s"] = True
            if y < height and p["s"]: pipeMap[y * 2 + 1][x * 2]["n"] = True

    distances = dict()
    queue = [(start, 0)]

    while queue:
        pos, dist = queue.pop(0)
        if pos in distances: continue
        distances[pos] = dist
        node = pipeMap[pos[1]][pos[0]]
        if node["e"]: queue.append(((pos[0] + 1, pos[1]), dist + 1))
        if node["w"]: queue.append(((pos[0] - 1, pos[1]), dist + 1))
        if node["n"]: queue.append(((pos[0], pos[1] - 1), dist + 1))
        if node["s"]: queue.append(((pos[0], pos[1] + 1), dist + 1))

    directlyConnectedOut = []
    for line in pipeMap:
        directlyConnectedOut.append([])
        for p in line:
            directlyConnectedOut[-1].append(False)

    queue = []
    for x in range(0, len(pipeMap[0])):
        queue.append((x, 0))
        queue.append((x, len(pipeMap) - 1))
    for y in range(0, len(pipeMap) - 1):
        queue.append((0, y))
        queue.append((len(pipeMap[0]) - 1, y))
    
    while queue:
        pos = queue.pop(0)
        if pos[0] < 0 or pos[0] >= len(pipeMap[0]): continue
        if pos[1] < 0 or pos[1] >= len(pipeMap): continue
        if pos in distances: continue
        if directlyConnectedOut[pos[1]][pos[0]]: continue
        directlyConnectedOut[pos[1]][pos[0]] = True
        for xOff in [-1, 0, 1]:
            for yOff in [-1, 0, 1]:
                queue.append((pos[0] + xOff, pos[1] + yOff))

    return countIn(pipeMap, distances, directlyConnectedOut)

def countIn(pipeMap, distances, connectedOut):
    ans = 0
    for y, line in enumerate(pipeMap):
        if y % 2 == 1: continue
        for x, p in enumerate(line):
            if x % 2 == 1: continue
            if (x, y) not in distances and not connectedOut[y][x]: 
                ans += 1
    return ans

def printMap(pipeMap, distances, connectedOut):
    for y, line in enumerate(pipeMap):
        if y % 2 == 1: continue
        for x, p in enumerate(line):
            if x % 2 == 1: continue
            if (x, y) in distances: 
                if (p == {"w": False, "e": True, "n": True, "s": False}): print("└", end="")
                elif (p == {"w": True, "e": False, "n": False, "s": True}): print("┐", end="")
                elif (p == {"w": True, "e": False, "n": True, "s": False}): print("┘", end="")
                elif (p == {"w": False, "e": True, "n": False, "s": True}): print("┌", end="")
                elif (p == {"w": True, "e": True, "n": False, "s": False}): print("─", end="")
                elif (p == {"w": False, "e": False, "n": True, "s": True}): print("│", end="")
                elif (p == {"w": False, "e": False, "n": False, "s": False}): print(".", end="")
                else: print("x", end="")
            else:
                if connectedOut[y][x]: print("O", end="")
                else: print("I", end="")
        print()

if __name__ == "__main__":
    print(f"The answer is {main()}")