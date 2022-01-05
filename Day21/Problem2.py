from pprint import pprint

limit =21

positions = [4, 8]
scores = [0, 0]
playerId = 0

playerWins = [0, 0]

scoresP1 = {}
scoresP2 = {}
results = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def main(player, position, score, waysP1=1, waysP2=1, diceResults=[]):
    #print(position, score, ways, diceResults)
    print(player, score, diceResults, max(waysP1, waysP2))

    if score < limit:
        for result, count in results.items():
            newPosition = (position + result) % 10
            if newPosition == 0: newScore = score + 10
            else: newScore = score + newPosition
            newWays1 = waysP1
            newWays2 = waysP2
            if player==1: newWays1 *= count
            else: newWays2 *= count
            main(player, newPosition, newScore, newWays1, newWays2, [i for i in diceResults] + [result])

    if player == 1:
        if score not in scoresP1: scoresP1[score] = {}
        if len(diceResults) not in scoresP1[score]: scoresP1[score][len(diceResults)] = 0
        scoresP1[score][len(diceResults)] += waysP1
    elif player == 2:
        if score not in scoresP2: scoresP2[score] = {}
        if len(diceResults) not in scoresP2[score]: scoresP2[score][len(diceResults)] = 0
        scoresP2[score][len(diceResults)] += waysP2



main(1, 4, 0)
main(2, 8, 0)
# pprint(scoresP1)
# pprint(scoresP2)

player1Wins = 0
player2Wins = 0

# for score, lengths in scoresP1.items():
#     if score < limit: continue

#     for length, count in lengths.items():

#         for p2Score, lengthsp2 in scoresP2.items():
#             if score > p2Score:
#                 if length-1 in lengthsp2: 
#                     player1Wins += count * lengthsp2[length-1]

for p1Score, p1Lengths in scoresP1.items():
    for p1Length, p1Count in p1Lengths.items():
        for p2Score, p2Lengths in scoresP2.items():
            for p2Length, p2Count in p2Lengths.items():
                if p1Score > p2Score and p1Score >= 21 and p1Length == p2Length + 1:
                    # print(p1Score, p2Score, p1Count, p2Count)
                    player1Wins += p1Count * p2Count

for p1Score, p1Lengths in scoresP2.items():
    for p1Length, p1Count in p1Lengths.items():
        for p2Score, p2Lengths in scoresP1.items():
            for p2Length, p2Count in p2Lengths.items():
                if p1Score > p2Score and p1Score >= 21 and p1Length == p2Length + 1:
                    player2Wins += p2Count * p1Count

print(player1Wins, len(str(player1Wins)))
print(player2Wins, len(str(player2Wins)))
