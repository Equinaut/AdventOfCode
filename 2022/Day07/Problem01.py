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

answer = [0]
def calculateSize(file):
    if file[2] is None: return file[1]
    size = sum(size for f in file[2] if (size:=calculateSize(f)))
    if (size < 100_000): answer[0] += size
    return size

calculateSize(rootFolder)
print(f"The answer is {answer[0]}")