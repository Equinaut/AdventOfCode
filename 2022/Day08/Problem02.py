grid = dict()

# Load file into dictionary object, in the form of (x,y): height
with open("input.txt") as file:
    for j, line in enumerate(file.readlines()):
        for i, height in enumerate(line[:-1]):
            grid[(i, j)] = int(height)
    height = i
    width = j

def score(actualX, actualY):
    value = grid[(actualX, actualY)]
    L = R = U = D = None
    for distance in range(1, max(width, height)):
        if L is None:
            if actualX - distance <= 0: L = distance
            elif grid[actualX - distance, actualY] >= value: L = distance

        if R is None:
            if actualX + distance >= width: R = distance
            elif grid[actualX + distance, actualY] >= value: R = distance

        if U is None:
            if actualY - distance <= 0: U = distance
            elif grid[actualX, actualY - distance] >= value: U = distance

        if D is None:
            if actualY + distance >= height: D = distance
            elif grid[actualX, actualY + distance] >= value: D = distance
    L = L or 0
    R = R or 0
    U = U or 0
    D = D or 0
    return L * R * U * D

answer = max([score(x, y) for x in range(0, width) for y in range(0, height)])

print(f"The answer is {answer}")