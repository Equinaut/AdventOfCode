wins = [0, 0]

results = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
limit = 16


def main(turn, positions, scores, iterations=0):
    if iterations < 3:
        print(iterations * "    ", end="")
        print(iterations, turn, positions, scores)

    if max(scores) > limit:
        wins[turn]+=1
        return

    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                newPositions = [i for i in positions]
                newScores = [i for i in scores]

                newPositions[turn] += a+b+c
                newPositions[turn] = positions[turn] % 10

                if newPositions[turn] == 0: newScores[turn] += 10
                else: newScores[turn] += newPositions[turn]

                main( (turn + 1) % 2, [i for i in newPositions], [i for i in newScores], iterations+1)


main(1, [4, 8], [0, 0], 1)
print(wins)