def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            sets = line.split(": ")[1]
            winNumbers, haveNumbers = sets.split("|")
            winNumbers = {int(i) for i in winNumbers.split(" ") if i != ""}
            haveNumbers = [int(i) for i in haveNumbers.split(" ") if i != ""]
            score = 0
            for n in haveNumbers:
                if n in winNumbers:
                    if score == 0: score = 1
                    else: score *= 2
            ans += score
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")