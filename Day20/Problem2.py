image = []
with open("input.txt", "r") as file:
    imageEnhancementAlgorithm = file.readline()[:-1]
    print(file.readline())
    line = file.readline()
    while line != "":
        image.append(line[:-1])
        line = file.readline()
print(imageEnhancementAlgorithm)
print(" ")

for l, line in enumerate(image):
    image[l] = list(line)

    for x, char in enumerate(line):
        image[l][x] = char == "#"

# Enhancement

def printImage(image):
    for line in image:
        for char in line:
            if char:
                print("#", end="")
            else:
                print(" ", end="")
        print("|")


def enhance(image):
    newImage = []
    for line in image:
        newImage.append([])
        for x in line:
            newImage[-1].append(False)

    for y in range(1, len(image)-1):
        for x in range(1, len(image[0])-1):
            pixels = []
            for y2 in range(-1, 2):
                for x2 in range(-1, 2):
                    pixels.append(image[y + y2][x + x2])
            pixels = int("".join(["1" if i else "0" for i in pixels]), 2)

            newImage[y][x] = (imageEnhancementAlgorithm[pixels] == "#")

    for y, line in enumerate(newImage):
        for x, char in enumerate(line):
            image[y][x] = char

def countPixels(image):
    result = 0
    for line in image:
        for char in line:
            if char: result+=1
    return result

for i in range(0, 200):
    image.insert(0, [False] * len(image[0]))
    image.append([False] * len(image[0]))

for i in range(0, 200):
    for y in range(0, len(image)):
        image[y].insert(0, False)
        image[y].append(False)

printImage(image)
for i in range(0, 50):
    print(i)
    enhance(image)
print("Enhanced")

image = [line[50:-50] for line in image[50:-50]]
printImage(image)


print(f"The answer is {countPixels(image)}")