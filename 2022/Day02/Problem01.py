# A - X = Rock
# B - Y = Paper
# C - Z = Scissors

moves = "ABC"
convertMoves = lambda x : chr(ord(x) - 23) # Converts from XYZ moves to ABC moves

def determineOutcome(opp, me):
    if me == moves[(moves.index(opp) + 1) % 3]: return 6
    elif opp == me: return 3
    return 0

answer = 0

with open("input.txt") as file:
    for line in file.readlines():
        opp, me = line[:-1].split(" ")
        answer += moves.index(convertMoves(me)) + 1
        answer += determineOutcome(opp, convertMoves(me))

print(f"The answer is {answer}")