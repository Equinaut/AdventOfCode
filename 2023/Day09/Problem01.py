def main():
    ans = 0
    with open("input.txt") as file:
        for line in file.readlines():
            ans += calculateNext([int(i) for i in line.split(" ")])
    return ans

def calculateNext(history):
    rows = [history]
    while not all(j == 0 for j in rows[-1]):
        newRow = []
        for i in range(1, len(rows[-1])):
            newRow.append(rows[-1][i] - rows[-1][i - 1])
        rows.append(newRow)

    rows[-1].append(0)
    for i in range(len(rows) - 2, -1, -1):
        diff = rows[i + 1][-1]
        rows[i].append(diff + rows[i][-1])
    return rows[i][-1]

if __name__ == "__main__":
    print(f"The answer is {main()}")