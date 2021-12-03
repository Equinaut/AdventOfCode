numbers = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append([int(i) for i in list(line[:-1])])

numbers2 = [[j for j in i] for i in numbers]

def genMostCommon(numberList, bitPosition, equalCase = True):
    ones = 0
    notOnes = 0
    for i, row in enumerate(numberList):
        if row[bitPosition] == 1: ones+=1
        else: notOnes +=1
    
    return {True: 1, False: 0}[ones>notOnes or (ones==notOnes and equalCase)]

for i in range(0, len(numbers[0])):
    mostCommonBit = genMostCommon(numbers, i)
    for j, row in enumerate(numbers):
        if row[i] != mostCommonBit:
            numbers[j] = None
    while None in numbers: numbers.remove(None)
    if len(numbers) == 1:
        break

for i in range(0, len(numbers2[0])):
    mostCommonBit = genMostCommon(numbers2, i, equalCase=True)

    for j, row in enumerate(numbers2):
        if row[i] == mostCommonBit:
            numbers2[j] = None
    while None in numbers2:
        numbers2.remove(None)
    if len(numbers2) == 1:
        break

oxygen = int("".join([str(i) for i in numbers[0]]), 2)
co2 = int("".join([str(i) for i in numbers2[0]]), 2)


print(f"The answer is {oxygen * co2}")
