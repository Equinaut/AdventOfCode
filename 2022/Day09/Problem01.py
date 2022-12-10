head = (0, 0)
tail = (0, 0)

def updateTail(head,tail): # Calculate new location of tail
    if min((a:=abs(head[0]-tail[0])),(b:=abs(head[1]-tail[1])))>=0 and max(a,b)>1:
        if head[0]>tail[0]: tail=(tail[0]+1,tail[1])
        if head[0]<tail[0]: tail=(tail[0]-1,tail[1])
        if head[1]>tail[1]: tail=(tail[0],tail[1]+1)
        if head[1]<tail[1]: tail=(tail[0],tail[1]-1)
    return tail

tailLocations = set()

with open("input.txt") as file:
    for line in file.readlines():
        direction = line[0]
        length = int(line[2:])
        for i in range(0, length):
            if (direction=="R"): head = (head[0] + 1, head[1])
            if (direction=="L"): head = (head[0] - 1, head[1])
            if (direction=="U"): head = (head[0], head[1] + 1)
            if (direction=="D"): head = (head[0], head[1] - 1)
            tail = updateTail(head, tail)
            tailLocations.add(tail)

print(f"The answer is {len(tailLocations)}")