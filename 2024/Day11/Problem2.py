blinkCache = dict()
def blink(n):
    if n in blinkCache: return blinkCache[n]
    newNumbers = []
    if n == 0: 
        newNumbers.append(1)
    elif len(str(n)) % 2 == 0:
        l = len(str(n))
        newNumbers.append(int(str(n)[:l//2]))
        newNumbers.append(int(str(n)[l//2:]))
    else:
        newNumbers.append(n * 2024)
    blinkCache[n] = newNumbers
    return newNumbers

splitStoneCache = dict()
def splitStone(n, splitCount):
    if splitCount == 0: return 1
    if (n, splitCount) in splitStoneCache: return splitStoneCache[n, splitCount]

    ans = sum(splitStone(stone, splitCount - 1) for stone in blink(n))
    splitStoneCache[(n, splitCount)] = ans
    return ans

def main():
    with open("input.txt") as file:
        numbers = list(map(int, file.read().split(" ")))
    ans = sum(splitStone(n, 75) for n in numbers)
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")