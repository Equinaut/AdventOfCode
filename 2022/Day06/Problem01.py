def main(text):
    for i in range(0, len(text) - 3):
        if len(set(text[i:i+4])) == 4: return i + 4

with open("input.txt") as file:
    answer = main(file.read())

print(f"The answer is {answer}")