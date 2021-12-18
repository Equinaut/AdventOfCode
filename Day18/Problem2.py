import math
import copy

numbers = []
with open("input.txt", "r") as file:
    for line in file:
        numbers.append(eval(line[:-1]))


def depth(snailNumber):  # Returns maximum depth of tree
    if type(snailNumber) == int:
        return 1
    return max(depth(snailNumber[0]), depth(snailNumber[1])) + 1


def shouldExplode(snailNumber):  # Returns True if tree needs to explode
    return depth(snailNumber) > 5


def maxNumber(snailNumber):  # Returns highest value in tree
    if type(snailNumber) == int:
        return snailNumber
    return max(maxNumber(snailNumber[0]), maxNumber(snailNumber[1]))


def shouldSplit(snailNumber):  # Returns True, if tree needs to be split
    return maxNumber(snailNumber) >= 10


def split(snailNumber):  # Splits the tree
    if type(snailNumber) == int:
        return
    if type(snailNumber[0]) == int and snailNumber[0] >= 10:
        num = snailNumber[0]
        snailNumber[0] = [math.floor(num / 2), math.ceil(num / 2)]
        return True
    if type(snailNumber[0]) == list:
        result = split(snailNumber[0])
        if result:
            return True

    if type(snailNumber[1]) == int and snailNumber[1] >= 10:
        num = snailNumber[1]
        snailNumber[1] = [math.floor(num / 2), math.ceil(num / 2)]
        return True
    if type(snailNumber[1]) == list:
        result = split(snailNumber[1])
        if result:
            return True
    return False


def explode(snailNumber, snailNumberWhole, depth=1, itemsSoFar=0):  # Explodes the tree
    if type(snailNumber) == int:
        return

    if type(snailNumber[0]) == list:
        if depth >= 4 and type(snailNumber[0][0]) == int and type(snailNumber[0][1]) == int:
            if itemsSoFar < treeSize(snailNumberWhole) - 1:
                setNthItem(snailNumberWhole, itemsSoFar + 2,
                           findNthItem(snailNumberWhole, itemsSoFar + 2) + snailNumber[0][1])
            if itemsSoFar > 0:
                setNthItem(snailNumberWhole, itemsSoFar - 1,
                           findNthItem(snailNumberWhole, itemsSoFar - 1) + snailNumber[0][0])
            snailNumber[0] = 0
            return True
        else:
            result = explode(
                snailNumber[0], snailNumberWhole, depth + 1, itemsSoFar)
            if result:
                return True

    if type(snailNumber[1]) == list:
        if depth >= 4 and type(snailNumber[1][0]) == int and type(snailNumber[1][1]) == int:
            if itemsSoFar < treeSize(snailNumberWhole) - 1:
                setNthItem(snailNumberWhole, itemsSoFar + 3,
                           findNthItem(snailNumberWhole, itemsSoFar + 3) + snailNumber[1][1])
            if itemsSoFar >= 0:
                setNthItem(snailNumberWhole, itemsSoFar, findNthItem(
                    snailNumberWhole, itemsSoFar) + snailNumber[1][0])
            snailNumber[1] = 0
            return True
        else:
            result = explode(snailNumber[1], snailNumberWhole,
                             depth + 1, itemsSoFar + treeSize(snailNumber[0]))
            if result:
                return True
    return False


def treeSize(snailNumber):  # Returns size of tree parse in
    if type(snailNumber) == int:
        return 1
    return treeSize(snailNumber[0]) + treeSize(snailNumber[1])


def findNthItem(snailNumber, n):  # Finds nth item from left to right in tree
    if type(snailNumber) == int:
        return snailNumber
    if n >= treeSize(snailNumber[0]):
        return findNthItem(snailNumber[1], n - treeSize(snailNumber[0]))
    return findNthItem(snailNumber[0], n)


def setNthItem(snailNumber, n, value):  # Sets value of nth item in tree, from left to right
    if type(snailNumber) == int:
        return

    if n == 0 and type(snailNumber[0]) == int:
        snailNumber[0] = value
        return
    if n == treeSize(snailNumber[0]) and type(snailNumber[1]) == int:
        snailNumber[1] = value
        return

    if n >= treeSize(snailNumber[0]):
        return setNthItem(snailNumber[1], n - treeSize(snailNumber[0]), value)
    return setNthItem(snailNumber[0], n, value)


def reduce(snailNumber):
    while True:
        actionDone = False
        while shouldExplode(snailNumber):
            explode(snailNumber, snailNumber)
            actionDone = True
        if shouldSplit(snailNumber):
            split(snailNumber)
            actionDone = True
        if not actionDone:
            return


def magnitude(snailNumber):
    if type(snailNumber) == int:
        return snailNumber
    return magnitude(snailNumber[0]) * 3 + magnitude(snailNumber[1]) * 2


largestMagnitude = 0

for number in numbers: reduce(number)

for number in numbers:
    for number2 in numbers:
        if number==number2: continue
        operand1 = copy.deepcopy(number)
        operand2 = copy.deepcopy(number2)
        result = [operand1, operand2]
        reduce(result)
        resultMagitude = magnitude(result)
        if resultMagitude > largestMagnitude: largestMagnitude = resultMagitude

print(f"The answer is {largestMagnitude}")