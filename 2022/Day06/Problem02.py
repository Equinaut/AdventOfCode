n = 14

def main(text):
    for i in range(0, len(text) - n + 1):
        if len(set(text[i:i+n])) == n: return i + n

with open("input.txt") as file:
    answer = main(file.read())

print(f"The answer is {answer}")