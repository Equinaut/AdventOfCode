def main():
    ans = 0
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

            workflowRules[workflow] = (outrules, rules[-1])

        for line in file:
            part = tuple([int(a.split(",")[0]) for a in line[1:-2].split("=")[1:]])

            workflow = "in"
            while workflow not in "AR":
                rules, outWorkflow = workflowRules[workflow]
                for rule in rules:
                    if rule[1] == "<": compare = lambda a, b: a < b
                    else: compare = lambda a, b: a > b

                    if rule[0] == "x": val = part[0]
                    elif rule[0] == "m": val = part[1]
                    elif rule[0] == "a": val = part[2]
                    elif rule[0] == "s": val = part[3]

                    if compare(val, rule[2]): 
                        workflow = rule[3]
                        break
                else:
                    workflow = outWorkflow
            if workflow == "A": ans += sum(part)
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")