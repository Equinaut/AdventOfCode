from itertools import permutations

answer = 0
signals = []

correctDigitsNumber = [set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"), set("abdfg"), set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg")]

with open("input.txt", "r") as file:
    for line in file.readlines():
        signals.extend([(line.split(" | ")[0].split(" "), line[:-1].split(" | ")[1].split(" "))])

def convertDigit(digit, permutation):
    #Converts segments turned on in a mixed up display, and a possible wireing, into the digit when rewired
    newDigit = set()
    for d in digit:
        for i, letter in enumerate(permutation):
            if d == letter: newDigit.add("abcdefg"[i])
    if newDigit in correctDigitsNumber:
        return correctDigitsNumber.index(newDigit)
    return None

i=0
for initalSignals, outputs in signals:
    print(i)
    i+=1
    for permutation in permutations("abcdefg"): #Check all possible wireings of display
        invalid = False
        for number in initalSignals:
            actualDigit = convertDigit(number, permutation)
            if actualDigit is None: invalid = True
        if invalid: continue
        else:
            thisNumber = 0
            thisNumber += convertDigit(outputs[0], permutation) * 1000
            thisNumber += convertDigit(outputs[1], permutation) * 100
            thisNumber += convertDigit(outputs[2], permutation) * 10
            thisNumber += convertDigit(outputs[3], permutation)
            answer+=thisNumber

print(f"The answer is {answer}")