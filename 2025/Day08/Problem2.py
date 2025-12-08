import heapq

def distance(p1, p2):
    return sum(pow(a - b, 2) for (a, b) in zip(p1, p2))

def main():
    positions = []
    with open("input.txt") as file:
        positions = [tuple(map(int, line[:-1].split(","))) for line in file]

    # Initialise circuit number for each junction box
    circuits = [i for i in range(0, len(positions))] 
    circuitCount = len(positions)
    
    h = []
    for i in range(0, len(positions)):
        for j in range(0, i):
            # Create heap with distances between each pair of circuits
            heapq.heappush(h, (distance(positions[i], positions[j]), i, j))
            
    while h and circuitCount > 1:
        d, i, j = heapq.heappop(h)
        if circuits[i] != circuits[j]: circuitCount -= 1
        # Repeatedly pop the closest pair of junction boxes off of the heap and merge them
        minCNumber = min(circuits[i], circuits[j])
        maxCNumber = max(circuits[i], circuits[j])
        # Merge the two circuits by setting all values with the higher circuit number to the lower circuit number
        for k in range(0, len(circuits)):
            if circuits[k] == maxCNumber: circuits[k] = minCNumber

    # Return product of X coords of final pair merged
    return positions[i][0] * positions[j][0]

if __name__ == "__main__":
    print(f"The answer is {main()}")
