def main():
    positions = set()
    with open("input.txt") as file:
        for y, line in enumerate(file):
            for x, c in enumerate(line):
                if c == ".":
                    positions.add((x, y))
                if c == "S": 
                    start = (x, y)
                    positions.add((x, y))
    
    return singleMapReachable(positions, start, 64)

def singleMapReachable(positions, start, moves):
    reachablePositions = set()
    reachablePositions.add(start)

    for i in range(moves):
        newReachablePositions = set()
        for pos in reachablePositions:
            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newNode = (pos[0] + offset[0], pos[1] + offset[1])
                if newNode not in positions: continue
                newReachablePositions.add(newNode)
        reachablePositions = newReachablePositions
    
    return len(reachablePositions)

if __name__ == "__main__":
    print(f"The answer is {main()}")