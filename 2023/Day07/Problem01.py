def main():
    ans = 0
    with open("input.txt") as file:
        ranks = [[] for _ in range(8)]
        for line in file:
            hand, score = line.split(" ")
            score = int(score)
            ranks[getRank(hand)].append((hand, score))
    j = 1
    for r in ranks:
        for c in sorted(r, key = lambda r1: handValue(r1[0])):
            ans += c[1] * j
            j += 1

    return ans

def getRank(hand):
    counts = {c: hand.count(c) for c in hand}
    rank = 0
    if 5 in counts.values(): rank = 7 # five of a kind
    elif 4 in counts.values(): rank = 6 # four Of a kind
    elif 3 in counts.values() and 2 in counts.values(): rank = 5 # full house
    elif 3 in counts.values(): rank = 4 # three Of a kind
    elif list(counts.values()).count(2) == 2: rank = 3 # two pair
    elif list(counts.values()).count(2) == 1: rank = 2 # one pair
    else: rank = 1 # high card
    return rank

def handValue(hand):
    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value = sum((15 ** i) * (values[hand[4 - i]] if hand[4 - i] in values else int(hand[4 - i])) for i in range(5))
    return value

if __name__ == "__main__":
    print(f"The answer is {main()}")