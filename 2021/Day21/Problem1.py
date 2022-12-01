with open("input.txt") as file:
    player1Start = int(file.readline().split(": ")[1])
    player2Start = int(file.readline().split(": ")[1])

positions = [player1Start, player2Start]
scores = [0, 0]
playerId = 0
totalDiceRolls = 0
nextDiceValue = (d for d in range(1, 1000))

while max(scores) < 1000:
    dicesRolls = [next(nextDiceValue) for i in range(0, 3)]
    totalDiceRolls += 3
    
    positions[playerId] += sum(dicesRolls)
    positions[playerId] = positions[playerId] % 10

    if positions[playerId] == 0: scores[playerId] += 10
    else: scores[playerId] += positions[playerId]

    playerId = (playerId + 1) % len(scores)

print(f"The answer is {totalDiceRolls * min(scores)}")