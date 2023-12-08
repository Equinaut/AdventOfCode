def main():
    leftNodes = dict()
    rightNodes = dict()
    with open("input.txt") as file:
        rightLeft = file.readline()[:-1]
        file.readline()
        for line in file.readlines():
            start, end = line[:-1].split(" = ")
            l, r = end[1: -1].split(", ")
            leftNodes[start] = l
            rightNodes[start] = r
    
    currentNode = "AAA"
    i = 0
    while currentNode != "ZZZ":
        if rightLeft[i % len(rightLeft)] == "R": currentNode = rightNodes[currentNode]
        else: currentNode = leftNodes[currentNode]
        i += 1
    return i

if __name__ == "__main__":
    print(f"The answer is {main()}")