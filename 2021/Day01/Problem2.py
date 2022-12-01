with open("input.txt", "r") as file:
    numbers = [int(i) for i in file.readlines()]

answer = 0
for i in range(0, len(numbers)-3):
    if sum(numbers[i:i+3]) < sum(numbers[i+1:i+4]): answer+=1

print(f"The answer is {answer}")