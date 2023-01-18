class Monkey:
    def __init__(self, name, operation: str):
        self.name = name
        if operation.isnumeric():
            self.value = int(operation)
        else:
            self.value = operation.split(" ")

    def getValue(self):
        if type(self.value) == int or type(self.value) == float:
            return self.value
        else:
            monkey1 = monkeys[self.value[0]]
            monkey2 = monkeys[self.value[2]]

            if self.value[1] == "-":
                return monkey1.getValue() - monkey2.getValue()
            if self.value[1] == "+":
                return monkey1.getValue() + monkey2.getValue()
            if self.value[1] == "*":
                return monkey1.getValue() * monkey2.getValue()
            if self.value[1] == "/":
                return monkey1.getValue() // monkey2.getValue()
monkeys = dict()

with open("input.txt") as file:
    for line in file.readlines():
        name, operation = line[:-1].split(": ")
        monkeys[name] = Monkey(name, operation)

answer = monkeys["root"].getValue()
print(f"The answer is {answer}")