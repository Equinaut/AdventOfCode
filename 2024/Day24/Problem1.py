def main():
    initialValues = dict()
    equations = dict()

    # Parse input
    with open("input.txt") as file:
        while (line := file.readline()) != "\n":
            var = line.split(": ")[0]
            initialValues[var] = line[:-1].split(": ")[1]

        while (line := file.readline()) != "":
            outputVal = line[:-1].split(" -> ")[1]
            args = line[:-1].split(" -> ")[0]
            equations[outputVal] = args
    
    finalValues = dict()
    zValues = [item for item in equations if item[0] == "z"]
    stack = [item for item in equations if item[0] == "z"]

    while stack:
        current = stack.pop()
        if current in finalValues: continue
        if current in initialValues: finalValues[current] = initialValues[current]
        else:
            preReqs = [equations[current].split(" ")[0], equations[current].split(" ")[2]]
            if all(item in finalValues for item in preReqs):
                arg0Val = finalValues[preReqs[0]]
                arg1Val = finalValues[preReqs[1]]
                operator = equations[current].split(" ")[1]
                if operator == "AND": finalValues[current] = "1" if (arg0Val == "1" and arg1Val == "1") else "0"
                elif operator == "OR": finalValues[current] = "1" if (arg0Val == "1" or arg1Val == "1") else "0"
                elif operator == "XOR": finalValues[current] = "1" if ((arg0Val == "1") != (arg1Val == "1")) else "0"
            else:
                stack.append(current)
                for item in preReqs:
                    if item not in finalValues: stack.append(item)
    result = 0
    for zVal in zValues: result |= int(finalValues[zVal]) << (int(zVal[1:]))
    return result

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")