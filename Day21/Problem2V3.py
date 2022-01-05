with open("input.txt") as file:
    player1Start = int(file.readline().split(": ")[1])
    player2Start = int(file.readline().split(": ")[1])

results = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

seenBefore = {}

def main(person, positions, scores, result):
    currentInput = str((person, positions, scores, result))
    if currentInput in seenBefore: return seenBefore[currentInput]

    seenBefore[currentInput] = seenBefore.get(currentInput, 0) + 1

    positions[person] += result
    positions[person] = positions[person] % 10
    if positions[person] == 0: scores[person] += 10
    else: scores[person] += positions[person]
    
    if max(scores) >= 21:
        if scores[0] > scores[1]:
            seenBefore[currentInput] = (1, 0)
            return (1, 0)
        else:
            seenBefore[currentInput] = (0, 1)
            return (0, 1)

    answer = (0, 0)
    for newResult, count in results.items():
        tempWins = main((person + 1) % 2, [i for i in positions], [i for i in scores], newResult)
        answer = (answer[0] + tempWins[0] * count, answer[1] + tempWins[1] * count)
    seenBefore[currentInput] = answer
    return answer


answer = (0, 0)
for result, count in results.items():
    tempWins = main(0, [player1Start, player2Start], [0, 0], result)
    answer = (answer[0] + tempWins[0] * count, answer[1] + tempWins[1] * count)

print(f"The answer is {max(answer)}")
