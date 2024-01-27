import copy

def main():
    with open("input.txt") as file:
        workflowRules = dict()

        for line in file:
            if line == "\n": break
            workflow,rules = line[:-2].split("{")
            rules = rules.split(",")
            outrules = []
            for rule in rules[:-1]:
                var = rule[0]
                comp = rule[1]
                num = int(rule[2:].split(":")[0])
                out = rule.split(":")[1]

                outrules.append((var, comp, num, out))

            while outrules and outrules[-1][3] == rules[-1]:
                outrules.pop()
            workflowRules[workflow] = (outrules, rules[-1])


    nextWorkflows = {w: [] for w in workflowRules}
    for w in workflowRules:
        for (_, _, _, w2) in workflowRules[w][0]:
            count = [i[0] for i in nextWorkflows[w]].count(w2)
            nextWorkflows[w].append((w2, count))
        w2 = workflowRules[w][1]
        count = [i[0] for i in nextWorkflows[w]].count(w2)
        nextWorkflows[w].append((w2, count))
    
    paths = []
    queue = [[("in", 0)]]

    while queue:
        path = queue.pop()
        if path[-1][0] == "A" or path[-1][0] == "R":
            paths.append(path)
            continue

        for next in nextWorkflows[path[-1][0]]:
            queue.append(copy.copy(path) + [next])
    
    ans = 0
    for path in paths:
        if path[-1][0] != "A": continue
        ranges = pathRanges(path, workflowRules)
        ans += totalAmount(*ranges)
    return ans

def totalAmount(*ranges):
    amount = 1
    for i in range(0, len(ranges), 2):
        amount *= ranges[i + 1] - ranges[i] + 1
    return amount

def pathRanges(path, workflowRules):
    minX, maxX, minM, maxM, minA, maxA, minS, maxS = 1, 4000, 1, 4000, 1, 4000, 1, 4000

    for i in range(0, len(path) - 1):
        minX, maxX, minM, maxM, minA, maxA, minS, maxS = newRanges(minX, maxX, minM, maxM, minA, maxA, minS, maxS, workflowRules, path[i], path[i + 1])
    return minX, maxX, minM, maxM, minA, maxA, minS, maxS

def newRanges(minX, maxX, minM, maxM, minA, maxA, minS, maxS, workflowRules, workflow, nextWorkflow):
    count = 0
    for rule in workflowRules[workflow[0]][0]:
        if rule[0] == "x": currentMin, currentMax = minX, maxX
        elif rule[0] == "m": currentMin, currentMax = minM, maxM
        elif rule[0] == "a": currentMin, currentMax = minA, maxA
        elif rule[0] == "s": currentMin, currentMax = minS, maxS

        if rule[3] == nextWorkflow[0] and count == nextWorkflow[1]:
                if rule[1] == ">":
                    currentMin = max(currentMin, rule[2] + 1)
                elif rule[1] == "<":
                    currentMax = min(currentMax, rule[2] - 1)

                if rule[0] == "x": return (currentMin, currentMax, minM, maxM, minA, maxA, minS, maxS)
                elif rule[0] == "m": return (minX, maxX, currentMin, currentMax, minA, maxA, minS, maxS)
                elif rule[0] == "a": return (minX, maxX, minM, maxM, currentMin, currentMax, minS, maxS)
                elif rule[0] == "s": return (minX, maxX, minM, maxM, minA, maxA, currentMin, currentMax)
        else:
            if rule[3] == nextWorkflow[0]: count += 1
            if rule[1] == ">":
                currentMax = min(currentMax, rule[2])
            elif rule[1] == "<":
                currentMin = max(currentMin, rule[2])

            if rule[0] == "x": minX, maxX = currentMin, currentMax
            elif rule[0] == "m": minM, maxM = currentMin, currentMax
            elif rule[0] == "a": minA, maxA = currentMin, currentMax
            elif rule[0] == "s": minS, maxS = currentMin, currentMax
    return (minX, maxX, minM, maxM, minA, maxA, minS, maxS)

if __name__ == "__main__":
    print(f"The answer is {main()}")
