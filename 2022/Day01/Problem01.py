currentTotal = 0
maxTotal = 0
with open("input.txt") as file:
    for line in file.readlines():
        if line.strip() == "": 
            currentTotal = 0
            continue
        currentTotal += int(line)
        if (currentTotal > maxTotal): maxTotal = currentTotal
        
print(f"The answer is {maxTotal}")