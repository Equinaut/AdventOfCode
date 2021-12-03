gammaRate = []
epsilonRate = []
lineCount = 0
with open("input.txt","r") as file:
    for line in file.readlines():
        lineCount+=1
        if gammaRate == []:
            gammaRate = [0] * (len(line) - 1)
        if epsilonRate == []:
            epsilonRate = [0] * (len(line) - 1)
        for i, bit in enumerate(line): 
            if (bit=="\n"): continue
            if bit == "1":
                gammaRate[i]+=1
            else:
                epsilonRate[i]+=1

print(lineCount)
gammaRate = [1 if i > (lineCount - i) else 0 for i in gammaRate]
epsilonRate = [1 if i==0 else 0 for i in gammaRate]

gammaRate = int("".join([str(i) for i in gammaRate]), 2)
epsilonRate = int("".join([str(i) for i in epsilonRate]), 2)

print(f"The answer is {gammaRate * epsilonRate}")
