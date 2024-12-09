import heapq

def main():
    gaps = []
    blocks = []
    ans = 0

    with open("input.txt") as file:
        pos = 0
        for i, c in enumerate(file.read()[:-1]):
            if i % 2 == 0:
                for j in range(0, int(c)): heapq.heappush(blocks, (-pos -j, i // 2))
            else:
                for j in range(0, int(c)): gaps.append(pos + j)
            pos += int(c)

    for firstGap in gaps:
        if -blocks[0][0] < firstGap: break
        heapq.heappushpop(blocks, (-firstGap, blocks[0][1]))
    
    ans = 0
    while blocks:
        block = heapq.heappop(blocks)
        ans -= block[0] * block[1]
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")