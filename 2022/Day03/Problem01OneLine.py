print(sum([(lambda l:(lambda c:c if c>0 else c+58)((lambda h:ord(list(set(l[:h]).intersection(l[h:]))[0])-96)(int(len(l)/2))))(line[:-1]) for line in open("input.txt")]))