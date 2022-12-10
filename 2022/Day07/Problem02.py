# folderStructure is represented as (Name, Size, [Children], Parent)
# file structure is represented as (Name, Size, None, Parent)

cwd = rootFolder = ("/", None, [], None)

with open("input.txt") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith("$ cd"): # Change directory
            name = line[5:-1]
            if name == "..": # Go to parent directory
                cwd = cwd[3]
            else:  # Find directory in current directory
                for file in cwd[2]:
                    if file[0] == name:
                        cwd = file
        elif line == "$ ls\n": # List directories
            results = []
            while i+1 < len(lines) and not lines[i+1].startswith("$"): 
                results.append(lines[i+1])
                i+=1
            for result in results:
                if result.startswith("dir"): # Add new directory
                    cwd[2].append((result[:-1].split(" ")[1], 0, [], cwd))
                else: # Add new file
                    size, name = result[:-1].split(" ")
                    cwd[2].append((name, int(size), None, cwd))

directorySizes = []
def calculateSize(file, directorySizes):
    (name, size, children, _) = file
    if children is not None:
        size = 0
        for child in children: size += calculateSize(child, directorySizes)
        directorySizes.append((name, size))
    return size

totalSize = calculateSize(rootFolder, directorySizes)
toFree = totalSize - 40_000_000
directorySizes = [d for d in directorySizes if d[1] >= toFree]
answer = min(directorySizes, key=lambda d: d[1])[1]

print(f"The answer is {answer}")