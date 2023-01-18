def convertToNumber(num):
    num = list(num)
    result = 0
    values = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    place = 1
    while num:
        result += place * values[num.pop()]
        place *= 5
    return result

def convertFromNumber(num):
    if num == 0: return ""
    place = 1
    while place < abs(num): place *= 5
    place //=5
    values = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
    result = ""
    while place >= 1:
        digit = min(values.items(), key = lambda digit: abs(num - place * digit[0]))
        num -= place * digit[0]
        place //= 5
        result += digit[1]
    return result

answer = 0
with open("input.txt") as file:
    for line in file.readlines():
        answer += convertToNumber(line[:-1])

print(f"The answer is {convertFromNumber(answer)}")