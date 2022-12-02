moves = "ABC"
convertMoves = lambda x : chr(ord(x) - 23)

def determineOutcome(opponent, me):
    if me == moves[(moves.index(opponent) + 1) % 3]: return 6
    elif opponent == me: return 3
    return 0

answer = 0

with open("input.txt") as file:
    for line in file:
        opponent, me = line[:-1].split(" ")
        answer += moves.index(convertMoves(me)) * 3
        for points, myMove in enumerate(moves):
            if determineOutcome(opponent, myMove) == moves.index(convertMoves(me)) * 3:
                answer += points + 1

print(f"The answer is {answer}")