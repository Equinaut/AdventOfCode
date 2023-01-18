class Monkey:
    def __init__(self, name, operation: str):
        self.name = name
        if operation.isnumeric():
            self.value = int(operation)
        else:
            self.value = operation.split(" ")

    def getValue(self):
        if self.name == "humn": return "HUMN", True
        if isinstance(self.value, int): return self.value, self.name == "humn"
        else:
            monkey1 = monkeys[self.value[0]]
            monkey2 = monkeys[self.value[2]]
            
            value1, reliesOnHumn1 = monkey1.getValue()
            value2, reliesOnHumn2 = monkey2.getValue()

            reliesOnHumn = reliesOnHumn1 or reliesOnHumn2 or self.name == "humn"

            if self.name == "root": return value1, value2
            if reliesOnHumn: return [value1, self.value[1], value2], reliesOnHumn

            if self.value[1] == "-": return value1 - value2, reliesOnHumn
            if self.value[1] == "+": return value1 + value2, reliesOnHumn
            if self.value[1] == "*": return value1 * value2, reliesOnHumn
            if self.value[1] == "/": return value1 // value2, reliesOnHumn

def calcValue(left, right):
    if left == "HUMN": return left, right
    value1, operation, value2 = left

    if isinstance(value1, int) or isinstance(value1, float):
        if operation == "-": return calcValue(value2, value1 - right)
        if operation == "+": return calcValue(value2, right - value1)
        if operation == "/": return calcValue(value2, value1 // right)
        if operation == "*": return calcValue(value2, right // value1)
    if isinstance(value2, int) or isinstance(value2, float):
        if operation == "-": return calcValue(value1, right + value2)
        if operation == "+": return calcValue(value1, right - value2)
        if operation == "/": return calcValue(value1, right * value2)
        if operation == "*": return calcValue(value1, right // value2)
    return left, right

def loadMonkeys():
    monkeys = dict()
    with open("input.txt") as file:
        for line in file.readlines():
            name, operation = line[:-1].split(": ")
            monkeys[name] = Monkey(name, operation)
    return monkeys

monkeys = loadMonkeys()
answer = calcValue(*monkeys["root"].getValue())[1]

print(f"The answer is {answer}")