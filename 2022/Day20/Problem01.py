numbers = []
list2 = []

with open("input.txt") as file:
    for i, line in enumerate(file.readlines()):
        numbers.append((int(line[:-1]), i))
        list2.append(i)

for i in range(0, len(numbers)):
    startIndex = list2.index(i)
    value = numbers[i][0]
    
    if value > 0:
        for j in range(0, value):
            list2[(startIndex + j)  % len(list2)], list2[(startIndex + j + 1)  % len(list2)] = list2[(startIndex + j + 1)  % len(list2)], list2[(startIndex + j)  % len(list2)]
    else:
        for j in range(0, value, -1):
            list2[(startIndex + j) % len(list2)], list2[(startIndex + j - 1)  % len(list2)] = list2[(startIndex + j - 1)  % len(list2)], list2[(startIndex + j)  % len(list2)]
newList = [numbers[i][0] for i in list2]

answer = sum([newList[(newList.index(0) + i) % len(newList)] for i in [1000, 2000, 3000]])
print(f"The answer is {answer}")