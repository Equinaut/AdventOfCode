from math import lcm

def main():
    leftNodes = dict()
    rightNodes = dict()
    currentNodes = []

    with open("input.txt") as file:
        rightLeft = file.readline()[:-1]
        file.readline()
        for line in file.readlines():
            start, end = line[:-1].split(" = ")
            l, r = end[1: -1].split(", ")
            leftNodes[start] = l
            rightNodes[start] = r
            if start[2] == "A": currentNodes.append(start)

    return lcm(*[getSeq(i, rightLeft, leftNodes, rightNodes) for i in currentNodes])

def getSeq(currentNode, rightLeft, leftNodes, rightNodes):
    i = 0
    while True:
        if rightLeft[i % len(rightLeft)] == "R": currentNode = rightNodes[currentNode]
        else: currentNode = leftNodes[currentNode]
        i += 1
        if currentNode[2] == "Z": break
    return i

if __name__ == "__main__":
    print(f"The answer is {main()}")