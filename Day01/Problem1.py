with open("input.txt", "r") as file:
    numbers = [int(i) for i in file.readlines()]

answer = 0
for i, j in enumerate(numbers[1:]):
    print(i, j, numbers[i])
    if j > numbers[i]: answer+=1

print(f"The answer is {answer}")