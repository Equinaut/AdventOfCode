def updateTail(head,tail): # Calculate new location of tail
    if min((a:=abs(head[0]-tail[0])),(b:=abs(head[1]-tail[1])))>=0 and max(a,b)>1:
        if head[0]>tail[0]: tail=(tail[0]+1,tail[1])
        if head[0]<tail[0]: tail=(tail[0]-1,tail[1])
        if head[1]>tail[1]: tail=(tail[0],tail[1]+1)
        if head[1]<tail[1]: tail=(tail[0],tail[1]-1)
    return tail

rope = [(0, 0)] * 10

tailLocations = set()
with open("input.txt") as file:
    for line in file.readlines():
        direction = line[0]
        length = int(line[2:])
        for i in range(0, length):
            if (direction=="R"): rope[0] = (rope[0][0] + 1, rope[0][1])
            if (direction=="L"): rope[0] = (rope[0][0] - 1, rope[0][1])
            if (direction=="U"): rope[0] = (rope[0][0], rope[0][1] + 1)
            if (direction=="D"): rope[0] = (rope[0][0], rope[0][1] - 1)
            for i in range(0, len(rope) - 1): rope[i + 1] = updateTail(rope[i], rope[i + 1])
            tailLocations.add(rope[-1])

print(f"The answer is {len(tailLocations)}")