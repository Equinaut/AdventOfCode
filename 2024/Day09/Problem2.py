import heapq

# Formula that uses triangle numbers to calculate the contribution to the final sum for a given file (position, size, fileNumber)
def calculateFileScore(file):
    return (file[1] + (file[0] * 2) - 1) * file[1] * file[2] // 2

def main():
    ans = 0

    # Heaps to keep track of positions of gaps
    gaps = [[] for _ in range(10)]
    # Stack to store file locations
    files = []

    with open("input.txt") as file:
        pos = 0
        for i, c in enumerate(file.read()[:-1]):
            fileSize = int(c)
            if i % 2 == 0: files.append((pos, fileSize, i // 2))
            else: heapq.heappush(gaps[fileSize], pos)
            pos += fileSize

    for lastFile in files[::-1]:
        # Find first gap that is large enough
        firstGap = None
        for size in range(lastFile[1], 10):
            if gaps[size] and (firstGap is None or gaps[size][0] < firstGap[0]) and gaps[size][0] < lastFile[0]:
                # If there is already a first gap then add this back to its heap, as an earlier one has been found
                if firstGap is not None: heapq.heappush(gaps[firstGap[1]], firstGap[0])

                firstGap = (heapq.heappop(gaps[size]), size)
                        
        if firstGap is None: # There is no gap large enough for this file, so it will not be moved
            ans += calculateFileScore(lastFile)
        else: # Move the file into the earliest large enough gap
            # Add the remaining space in the gap back to the gaps heap
            newGapSize = firstGap[1] - lastFile[1]
            if newGapSize: heapq.heappush(gaps[newGapSize], firstGap[0] + lastFile[1])
            ans += calculateFileScore((firstGap[0], lastFile[1], lastFile[2]))
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")