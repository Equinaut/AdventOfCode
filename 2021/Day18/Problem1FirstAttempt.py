"""
This was my first attempt at this problem, and does not work, but I thought I would include it anyway
"""

import math

numbers = []
with open("inputSmall.txt", "r") as file:
    for line in file.readlines():
        numbers.append(eval(line[:-1]))

numbers.reverse()

def explode(snailNumber):
    numString = str(snailNumber)
    numString = list(numString)
    while " " in numString: numString.remove(" ")
    numString = "".join(numString)

    i = 0
    depth = 0
    startOfBrakets = endOfBrackets = None
    while i < len(numString):
        if numString[i] == "[": depth+=1
        if numString[i] == "]": depth-=1
        if depth > 4 and numString[i] == "[" and numString[i+1].isdigit() and (numString[i+4] == "]" or numString[i+5]=="]" or numString[i+6]=="]"): 
            startOfBrakets = i
            break
        i+=1

    if startOfBrakets == None: return eval(numString)

    if numString[i+4]=="]": endOfBrackets = startOfBrakets + 4
    elif numString[i+5]=="]": endOfBrackets = startOfBrakets + 5
    elif numString[i+6]=="]": endOfBrackets = startOfBrakets + 6
    
    previousPosition = nextPosition = None
    i = startOfBrakets
    while i > 0 and not numString[i].isdigit(): i-=1
    if numString[i].isdigit(): previousPosition = i

    i = endOfBrackets
    while i < len(numString) - 1 and not numString[i].isdigit(): i+=1
    if numString[i].isdigit(): nextPosition = i
    offset = 0

    if previousPosition is not None and numString[previousPosition].isdigit():
        numString = list(numString)
        newNum = str(int(numString[previousPosition]) + int(numString[startOfBrakets + 1]))
        numString[previousPosition] = newNum
        offset = len(newNum) - 1
        numString = "".join(numString)
    
    if nextPosition is not None and numString[nextPosition+offset].isdigit():
        numString = list(numString)
        newNum = str(int(numString[nextPosition + offset]) + int(numString[endOfBrackets - 1 + offset]))
        numString[nextPosition + offset] = newNum
        numString = "".join(numString)
    
    numString = list(numString)
    numString[startOfBrakets + offset: endOfBrackets+1+offset] = "0"
    numString = "".join(numString)

    return eval(numString)

def split(snailNumber):
    numString = str(snailNumber)
    startPosition = None
    for i in range(0, len(numString)):
        if numString[i].isdigit() and numString[i+1].isdigit():
            startPosition = i
            break
    
    if startPosition is None: return eval(numString)

    endPosition = startPosition
    while numString[endPosition+1].isdigit(): endPosition+=1

    numberToReplace = int(numString[startPosition: endPosition+1])
    newValue = f"[{math.floor(numberToReplace/2)}, {math.ceil(numberToReplace/2)}]"
    numString = list(numString)
    numString[startPosition: endPosition+1]=newValue
    numString = "".join(numString)
    return eval(numString)

def shouldSplit(snailNumber):
    numString = str(snailNumber)
    for i in range(0, len(numString)):
        if numString[i].isdigit() and numString[i+1].isdigit(): return True
    return False

def reduce(snailNumber):
    while True:
        completedAction = False
        startValue = str(snailNumber)
        snailNumber = explode(snailNumber)
        while str(snailNumber) != startValue:
            startValue = str(snailNumber)
            snailNumber = explode(snailNumber)
            completedAction = True

        while shouldSplit(snailNumber):
            snailNumber = split(snailNumber)
            completedAction = True
        if not completedAction: break
    return snailNumber

def magnitude(snailNumber):
    if type(snailNumber)==int: return snailNumber
    return magnitude(snailNumber[0]) * 3 + magnitude(snailNumber[1]) * 2

while len(numbers) > 1:
    operand1 = reduce(numbers.pop())
    operand2 = reduce(numbers.pop())
    numbers.append(reduce([operand1, operand2]))
    print(numbers[-1])