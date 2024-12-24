import copy

def getEquation(node, equations, first = True, depth = 0):
    # Returns the equation of a certain node from the input graph
    # in terms of x and y values
    if node not in equations: return node
    else:
        if node[0] == "z" and not first: return node
        arg1 = getEquation(equations[node][0], equations, False, depth = depth + 1)
        arg2 = getEquation(equations[node][2], equations, False, depth = depth + 1)
        if arg1 is None or arg2 is None: return None

        if str(arg1) <= str(arg2): return (arg1, equations[node][1], arg2)
        else: return (arg2, equations[node][1], arg1)

def sortEquation(equation):
    # Sorts an equation into a canonical order
    if isinstance(equation, str): return equation
    else: 
        a, b = sortEquation(equation[0]), sortEquation(equation[2])
        if str(a) <= str(b): return (a, equation[1], b)
        else: return (b, equation[1], a)

def getCorrectEquation(bitNumber, carry = False):
    # Returns the correct equation for a certain stage of the binary adder process
    # in terms of x and y values

    # carry specifies whether to return the output bit value or the carry value

    if bitNumber == 0: 
        if carry: return ("x00", "AND", "y00")
        else: return ("x00", "XOR", "y00")
    else:
        num = str(bitNumber).zfill(2)
        carryIn = getCorrectEquation(bitNumber - 1, True)
        if carry: return sortEquation(((f"x{num}", "AND", f"y{num}"), "OR", ((f"x{num}", "XOR", f"y{num}"), "AND", carryIn)))
        else: return sortEquation(((f"x{num}", "XOR", f"y{num}"), "XOR", carryIn))

def simplifyEquation(equation, inputNodes):
    if equation in inputNodes: return inputNodes[equation]
    else: return (simplifyEquation(equation[0], inputNodes), equation[1], simplifyEquation(equation[2], inputNodes))

def getNextSwap(equations, inputNodes, bitLength):
    # Returns the values of the next two nodes that need to be swapped
    for c in range(0, bitLength):
        current = "z" + str(c).zfill(2)
        if current not in equations: return None

        currentResult = getEquation(current, equations)
        expectedResult = getCorrectEquation(c)

        if currentResult != expectedResult: 
            a = simplifyEquation(currentResult, inputNodes)
            b = simplifyEquation(expectedResult, inputNodes)
            while not (isinstance(a, str) and isinstance(b, str)):
                if isinstance(a, str): a = equations[a]
                if isinstance(b, str): b = equations[b]

                if a[0] == b[0] and a[1] == b[1]: a, b = a[2], b[2]
                elif a[2] == b[2] and a[1] == b[1]: a, b = a[0], b[0]
            return a, b
    return None

def swapEquations(equations, swap):
    # Applies swap to equations
    if equations is None: return None
    newEquations = copy.copy(equations)
    newEquations[swap[0]], newEquations[swap[1]] = newEquations[swap[1]], newEquations[swap[0]]

    inputNodes = dict()
    for var in newEquations:
        equation = getEquation(var, newEquations)
        if equation is None: continue
        inputNodes[equation] = var
    return newEquations, inputNodes

def main():
    equations = dict()

    # Parse the input file
    bitLength = 0
    with open("input.txt") as file:
        while (line := file.readline()) != "\n": continue

        while (line := file.readline()) != "":
            outputVal = line[:-1].split(" -> ")[1]
            args = line[:-1].split(" -> ")[0]
            # Equations stores the connections from the input file
            equations[outputVal] = sortEquation(args.split(" "))
            if outputVal[0] == "z": bitLength = max(int(outputVal[1:]), bitLength)

    inputNodes = dict()
    for var in equations:
        equation = getEquation(var, equations)
        if equation is not None: inputNodes[equation] = var

    # Set to store the list of values that are swapped
    swapValues = set()
    while ((nextSwap := getNextSwap(equations, inputNodes, bitLength)) is not None):
        equations, inputNodes = swapEquations(equations, nextSwap)
        swapValues |= set(nextSwap)

    return ",".join(sorted(swapValues))

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")