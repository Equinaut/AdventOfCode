def runProgram(instructions, a, b, c):
    output = []
    insPointer = 0
    while insPointer + 1 < len(instructions):
        ins, opp = instructions[insPointer], instructions[insPointer + 1]
        match opp:
            case 4: comboOpp = a % 8
            case 5: comboOpp = b % 8
            case 6: comboOpp = c % 8
            case _: comboOpp = opp

        opp %= 8
        jump = None
        match ins:
            case 0: a = int(a // 2 ** comboOpp)
            case 1: b ^= opp
            case 2: b = comboOpp % 8
            case 3: jump = opp if a != 0 else None
            case 4: b ^= c
            case 5: output.append(comboOpp)
            case 6: b = int(a // 2 ** comboOpp)
            case 7: c = int(a // 2 ** comboOpp) 
        insPointer = insPointer + 2 if jump is None else jump
    return ",".join(map(str, output))


def main():
    with open("input.txt") as file:
        a = int(file.readline().split(": ")[1])
        b = int(file.readline().split(": ")[1])
        c = int(file.readline().split(": ")[1])
        file.readline()
        instructions = list(map(int, file.readline().split(": ")[1].split(",")))

    return runProgram(instructions, a, b, c)

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")