def compare(left, right):
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
    for i, pair in enumerate(file.read()[:-1].split("\n\n")):
        left, right = map(eval, pair.split("\n"))
        if compare(left, right):
            answer += i + 1

print(f"The answer is {answer}")