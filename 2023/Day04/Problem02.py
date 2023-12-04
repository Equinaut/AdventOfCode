def main():
    ans = 0
    cards = dict()
    with open("input.txt") as file:
        for line in file:
            cardNumber, sets = line.split(": ")
            winNumbers, haveNumbers = sets.split("|")
            winNumbers = {int(i) for i in winNumbers.split(" ") if i != ""}
            haveNumbers = [int(i) for i in haveNumbers.split(" ") if i != ""]
            
            cards[int(cardNumber.split(" ")[-1])] = (winNumbers, haveNumbers)
            
        cardAmounts = dict()
        for card in cards:
            num = countMatches(*cards[card])
            if card not in cardAmounts: cardAmounts[card] = 1
            for i in range(card + 1, card + 1 + num):
                if i not in cardAmounts: cardAmounts[i] = 1 + cardAmounts[card]
                else: cardAmounts[i] += cardAmounts[card]

            ans = sum(cardAmounts.values())
    return ans

def countMatches(winNumbers, haveNumbers):
    score = 0
    for n in haveNumbers:
        if n in winNumbers:
            score += 1
    return score

if __name__ == "__main__":
    print(f"The answer is {main()}")