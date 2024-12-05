
def checkOrdering(nums, before):
    had = set()
    allNums = set(nums)
    for i in nums:
        needBefore = before.get(i, set()) & allNums
        if not had.issubset(needBefore): return False
        had.add(i)
    return True

def main():
    ans = 0
    before = dict()
    with open("input.txt") as file:
        for line in file:
            if "|" in line: 
                a,b = map(int, line.split("|"))
                if b not in before: before[b] = set()
                before[b].add(a)    
            elif "," in line: 
                nums = [int(i) for i in line.split(",")]
                allNums = set(nums)
                had = set()
                targetL = len(nums) // 2
                if not checkOrdering(nums, before):
                    actualOrder = []
                    while len(actualOrder) <= targetL:
                        for i in nums:
                            needBefore = before.get(i, set()) & allNums
                            if all(j in had for j in needBefore): 
                                nums.remove(i)
                                had.add(i)
                                actualOrder.append(i)
                    ans += actualOrder[targetL]
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")