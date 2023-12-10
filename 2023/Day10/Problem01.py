def main():
    pipeMap = []
    with open("input.txt") as file:
        for y, line in enumerate(file):
            pipeMap.append([])
            for x, p in enumerate(line[:-1]):
                if p == "S":
                    start = (x, y)
                    pipeMap[-1].append(None)
                else:
                    pipeMap[-1].append({
                        "w": p == "-" or p == "7" or p == "J",
                        "e": p == "-" or p == "L" or p == "F",
                        "n": p == "|" or p == "L" or p == "J",
                        "s": p == "|" or p == "7" or p == "F",
                    })

    pipeMap[start[1]][start[0]] = {
        "w": pipeMap[start[1]][start[0] - 1]["e"],
        "e": pipeMap[start[1]][start[0] + 1]["w"],
        "n": pipeMap[start[1] - 1][start[0]]["s"],
        "s": pipeMap[start[1] + 1][start[0]]["n"],
    }
    maxDist = 0
    distances = dict()
    queue = [(start, 0)]

    while queue:
        pos, dist = queue.pop(0)
        if pos in distances: continue
        distances[pos] = dist
        if dist > maxDist: maxDist = dist
        node = pipeMap[pos[1]][pos[0]]
        if node["e"]: queue.append(((pos[0] + 1, pos[1]), dist + 1))
        if node["w"]: queue.append(((pos[0] - 1, pos[1]), dist + 1))
        if node["n"]: queue.append(((pos[0], pos[1] - 1), dist + 1))
        if node["s"]: queue.append(((pos[0], pos[1] + 1), dist + 1))
    return maxDist

def printMap(pipeMap):
    for y, line in enumerate(pipeMap):
        for x, p in enumerate(line):
            if (p == {"w": False,"e": True,"n": True,"s": False}): print("└", end="")
            if (p == {"w": True,"e": False,"n": False,"s": True}): print("┐", end="")
            if (p == {"w": True,"e": False,"n": True,"s": False}): print("┘", end="")
            if (p == {"w": False,"e": True,"n": False,"s": True}): print("┌", end="")
            if (p == {"w": True,"e": True,"n": False,"s": False}): print("─", end="")
            if (p == {"w": False,"e": False,"n": True,"s": True}): print("│", end="")
            if (p == {"w": False,"e": False,"n": False,"s": False}): print(" ", end="")
        print()

if __name__ == "__main__":
    print(f"The answer is {main()}")