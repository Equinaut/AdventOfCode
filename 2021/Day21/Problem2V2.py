results = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

limit = 21
wins = [0, 0]
def main(turn, p1pos, p2pos, p1sc, p2sc, ways, roll, iterations):
    if iterations < 5: 
        print("\t" * iterations, end="")
        print(p1sc, p2sc, ways, roll, iterations)
    if turn==1:
        p1pos+=roll
        p1pos = p1pos % 10
        if p1pos==0: p1sc+=10
        else: p1sc += p1pos
    else:
        p2pos+=roll
        p2pos = p2pos % 10
        if p2pos==0: p2sc+=10
        else: p2sc += p2sc
    
    if p1sc >= 21 or p2sc >= 21: 
        wins[turn] += ways
        return

    for result, count in results.items():
        main((turn + 1) % 2, p1pos, p2pos, p1sc, p2sc, ways * count, result, iterations+1)
    

for result, count in results.items():
    print(result, count)
    main(0, 4, 8, 0, 0, count, result, 1)
print(wins)