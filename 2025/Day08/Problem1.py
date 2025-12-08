import heapq

def distance(p1, p2):
    return sum(pow(a - b, 2) for (a, b) in zip(p1, p2))

def main(connectionCount):
    positions = []
    with open("input.txt") as file:
        positions = [tuple(map(int, line[:-1].split(","))) for line in file]

    # Initialise circuit number for each junction box
    circuits = [i for i in range(0, len(positions))]
    
    h = []
    for i in range(0, len(positions)):
        for j in range(0, i):
            # Create heap with distances between each pair of circuits
            heapq.heappush(h, (distance(positions[i], positions[j]), i, j))

    while h and connectionCount > 0:
        d, i, j = heapq.heappop(h)
        connectionCount -= 1
        # Repeatedly pop the closest pair of junction boxes off of the heap and merge them
        minC, maxC = (circuits[i], circuits[j]) if (circuits[i] < circuits[j]) else (circuits[j], circuits[i])
        # Merge the two circuits by setting all values with the higher circuit number to the lower circuit number
        for k in range(0, len(circuits)):
            if circuits[k] == maxC: circuits[k] = minC
            
    # Calculate list of circuit sizes
    sizes = tuple(sorted([circuits.count(i) for i in set(circuits)], reverse=True))
    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    print(f"The answer is {main(1000)}")
