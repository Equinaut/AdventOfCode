import copy

def compare(left, right):
    left = copy.copy(left)
    right = copy.copy(right)
    if isinstance(left, int) and isinstance(right, int): return left <= right
    if isinstance(left, int): left = [left]
    if isinstance(right, int): right = [right]

    if len(left) == len(right) == 0: return True

    if len(right) == 0: return False
    if len(left) == 0: return True
    while left[0] == right[0]:
        left.pop(0)
        right.pop(0)
        if len(right) == 0: return False
        if len(left) == 0: return True

    return compare(left[0], right[0])

answer = 0
with open("input.txt") as file:
    a, b = 1, 2
    for line in file.readlines():
        if line == "\n": continue
        p = eval(line[:-1])
    
        if compare(p, [[2]]):  a += 1
        if compare(p, [[6]]):  b += 1

answer = a * b
print(f"The answer is {answer}")