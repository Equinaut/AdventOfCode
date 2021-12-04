class Grid:
    def __init__(self):
        self.lines = []

    def addToGrid(self, line):
        numbers = [int(i) if not i == "" else None for i in line[:-1].split(" ")]
        while None in numbers:
            numbers.remove(None)
        self.lines = self.lines + [numbers]

    def outputGrid(self):
        for line in self.lines:
            print(line)

    def readNumber(self, number):
        for i, row in enumerate(self.lines):
            for j, gridNumber in enumerate(row):
                if gridNumber == number:
                    self.lines[i][j] = None
                    return

    def hasWon(self):
        for row in self.lines:
            if all([i is None for i in row]):
                return True
        for i in range(0, len(self.lines[0])):
            if all([row[i] is None for row in self.lines]):
                return True

    def calculateScore(self):
        score = 0
        for row in self.lines:
            for i in row:
                if i == None:
                    continue
                score += i
        return score


with open("input.txt", "r") as file:
    lines = file.readlines()

numbers = [int(i) for i in lines[0].split(",")]

grids = [Grid()]
for line in lines[2:-1]:
    if line == "\n":
        grids.append(Grid())
        continue
    grids[-1].addToGrid(line)


gameOver = False
for number in numbers:
    for grid in grids:
        grid.readNumber(number)

        if grid.hasWon():
            print(f"The answer is {grid.calculateScore() * number}")
            gameOver = True
            break
    if gameOver:
        break
