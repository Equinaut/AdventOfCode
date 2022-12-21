class Monkey:
    def __init__(self, monkeyDescriptor):
        monkeyDescriptor = monkeyDescriptor.split("\n")
        self.name = monkeyDescriptor[0][:-1]
        self.items = list(map(int, monkeyDescriptor[1].split(": ")[1].split(", ")))
        self.operation = monkeyDescriptor[2].split(": ")[1][6:]

        self.test = monkeyDescriptor[3].split(": ")[1]
        self.ifTrue = int(monkeyDescriptor[4].split(": ")[1][16:])
        self.ifFalse = int(monkeyDescriptor[5].split(": ")[1][16:])

        self.inspectedItems = 0

    def __repr__(self):
        return f"Monkey(\"{self.name}\", {self.items})"

    def carryOutOperation(self, value):
        if self.operation == "old * old": return value * value

        operationValue = int(self.operation[6:])
        if self.operation[4] == "*":
            return value * operationValue
        if self.operation[4] == "+":
            return value + operationValue

    def carryOutTest(self, value):
        if self.test.startswith("divisible by "):
            divisor = int(self.test[13:])
            return value % divisor == 0
    
    def throw(self, value):
        self.items.append(value)

    def haveTurn(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspectedItems += 1
            item = self.carryOutOperation(item)
            item = item // 3
            
            if self.carryOutTest(item):
                monkeys[self.ifTrue].throw(item)
            else:
                monkeys[self.ifFalse].throw(item)

with open("input.txt") as file:
    sections = file.read().split("\n\n")
    monkeys = list(map(Monkey, sections))

for n in range(20):
    for monkey in monkeys:
        monkey.haveTurn()

monkeys.sort(key = lambda m : m.inspectedItems, reverse=True)
answer = monkeys[0].inspectedItems * monkeys[1].inspectedItems

print(f"The answer is {answer}")