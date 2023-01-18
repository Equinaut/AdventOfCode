import copy

numbers = []
list2 = []

with open("input.txt") as file:
    for i, line in enumerate(file.readlines()):
        numbers.append((int(line[:-1]) * 811589153, i))
        list2.append(i)

def listsEqual(list1, list2): 
    return list1 == list2[(index := list2.index(list1[0])):] + list2[:index]

for k in range(10):
    for i in range(0, len(numbers)):
        startIndex = list2.index(i)
        value = numbers[i][0]
        startNumbers = copy.copy(list2)

        if value > 0:
            for j in range(0, value % (len(list2) - 1)):
                list2[(startIndex + j) % len(list2)], list2[(startIndex + j + 1)  % len(list2)] = list2[(startIndex + j + 1)  % len(list2)], list2[(startIndex + j)  % len(list2)]
        else:
            for j in range(0, -1 * ((abs(value)) % (len(list2) - 1)), -1):
                list2[(startIndex + j) % len(list2)], list2[(startIndex + j - 1)  % len(list2)] = list2[(startIndex + j - 1)  % len(list2)], list2[(startIndex + j)  % len(list2)]

newList = [numbers[i][0] for i in list2]

indexOfZero = newList.index(0)
answer = sum(newList[(indexOfZero + i) % len(newList)] for i in [1000, 2000, 3000])
print(f"The answer is {answer}")