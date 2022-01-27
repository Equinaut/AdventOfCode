from math import floor


def execute(instructions, z, *numbers):
    w = x = y = 0
    numbers = list(numbers)

    for instruction in instructions:
        destination = instruction.split(" ")[1]
        if len(instruction.split(" ")) > 2:
            value2 = instruction.split(" ")[2]
            if value2 == "w":
                value2 = w
            elif value2 == "x":
                value2 = x
            elif value2 == "y":
                value2 = y
            elif value2 == "z":
                value2 = z
            else:
                value2 = int(value2)
        else:
            value2 = None

        if destination == "w":
            destinationValue = w
        elif destination == "x":
            destinationValue = x
        elif destination == "y":
            destinationValue = y
        elif destination == "z":
            destinationValue = z

        instruction = instruction.split(" ")[0]

        if instruction == "inp":
            destinationValue = numbers.pop(0)
        elif instruction == "add":
            destinationValue = destinationValue + value2
        elif instruction == "mul":
            destinationValue = destinationValue * value2
        elif instruction == "div":
            destinationValue = floor(destinationValue / value2)
        elif instruction == "mod":
            destinationValue = destinationValue % value2
        elif instruction == "eql":
            destinationValue = {True: 1, False: 0}[destinationValue == value2]

        if destination == "w":
            w = destinationValue
        elif destination == "x":
            x = destinationValue
        elif destination == "y":
            y = destinationValue
        elif destination == "z":
            z = destinationValue

    return w, x, y, z


instructionsImproved = [[]]
with open("inputImproved.txt", "r") as file:
    for line in file.readlines()[:-1]:
        if line == "\n":
            instructionsImproved.append([])
        else:
            instructionsImproved[-1].append(line[:-1])

instructions = []
with open("input.txt", "r") as file:
    for line in file.readlines()[:-1]:
        if line == "\n":
            instructions.append([])
        else:
            instructions.append(line[:-1])


def solve(part, zSet):
    zSets = {}
    for digit in range(9, 0, -1):
        newZSet = set()
        for z in zSet:
            newZSet.add(
                execute(instructionsImproved[part], 0, 0, 0, z, digit)[3])
        zSets[digit] = newZSet
    return zSets


first5Sections = []
next5Sections = []
lastSections = []
for i in instructionsImproved[:5]:
    first5Sections.extend(i)
for i in instructionsImproved[5:10]:
    next5Sections.extend(i)
for i in instructionsImproved[10:]:
    lastSections.extend(i)


def main():
    zSet1, zSet2, zSet3, zSet4, zSet5, zSet6, zSet7, zSet8, zSet9, zSet10, zSet11, zSet12, zSet13 = [
        set() for i in range(0, 13)]

    for d1 in range(1, 10):
        z = execute(instructionsImproved[0], 0, d1)[3]
        if z in zSet1:
            continue
        zSet1.add(z)

        for d2 in range(1, 10):
            z2 = execute(instructionsImproved[1], z, d2)[3]
            if z2 in zSet2:
                continue
            zSet2.add(z2)

            for d3 in range(1, 10):
                z3 = execute(instructionsImproved[2], z2, d3)[3]
                if z3 in zSet3:
                    continue
                zSet3.add(z3)

                for d4 in range(1, 10):
                    print(d1, d2, d3, d4)

                    z4 = execute(instructionsImproved[3], z3, d4)[3]
                    if z4 in zSet4:
                        continue
                    zSet4.add(z4)

                    for d5 in range(1, 10):
                        z5 = execute(instructionsImproved[4], z4, d5)[3]
                        if z5 in zSet5:
                            continue
                        zSet5.add(z5)

                        for d6 in range(1, 10):
                            z6 = execute(instructionsImproved[5], z5, d6)[3]
                            if z6 in zSet6:
                                continue
                            zSet6.add(z6)

                            for d7 in range(1, 10):
                                z7 = execute(
                                    instructionsImproved[6], z6, d7)[3]
                                if z7 in zSet7:
                                    continue
                                zSet7.add(z7)

                                for d8 in range(1, 10):
                                    z8 = execute(
                                        instructionsImproved[7], z7, d8)[3]
                                    if z8 in zSet8:
                                        continue
                                    zSet8.add(z8)

                                    for d9 in range(1, 10):
                                        z9 = execute(
                                            instructionsImproved[8], z8, d9)[3]
                                        if z9 in zSet9:
                                            continue
                                        zSet9.add(z9)

                                        for d10 in range(1, 10):
                                            z10 = execute(
                                                instructionsImproved[9], z9, d10)[3]
                                            if z10 in zSet10:
                                                continue
                                            zSet10.add(z10)

                                            for d11 in range(1, 10):
                                                z11 = execute(
                                                    instructionsImproved[10], z10, d11)[3]
                                                if z11 in zSet11:
                                                    continue
                                                zSet11.add(z11)

                                                for d12 in range(1, 10):
                                                    z12 = execute(
                                                        instructionsImproved[11], z11, d12)[3]
                                                    if z12 in zSet12:
                                                        continue
                                                    zSet12.add(z12)

                                                    for d13 in range(1, 10):
                                                        z13 = execute(
                                                            instructionsImproved[12], z12, d13)[3]
                                                        if z13 in zSet13:
                                                            continue
                                                        zSet13.add(z13)

                                                        for d14 in range(1, 10):
                                                            z14 = execute(
                                                                instructionsImproved[13], z13, d14)[3]
                                                            if z14 == 0:
                                                                print(
                                                                    "Found a solution")
                                                                print(
                                                                    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14)
                                                                print(
                                                                    z, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14)
                                                                return d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14


print(main())


"""
That's not the right answer. 
If you're stuck, make sure you're using the full input data; 
there are also some general tips on the about page, or you can ask for hints on the subreddit. 
Because you have guessed incorrectly 5 times on this puzzle, please wait 5 minutes before trying again. 
(You guessed 91599994399399.) 
[Return to Day 24]
"""
