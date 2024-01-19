def main():
    with open("input.txt") as file:
        parts = file.read().split(",")
        hashMap = [[] for i in range(256)]
        for part in parts:
            if "=" in part:
                label, b  = part.split("=")
                hashVal = hashString(label)
                indexOf = None
                for i, item in enumerate(hashMap[hashVal]): 
                    if item[0] == label:
                        indexOf = i
                        break
                if indexOf is None: hashMap[hashVal].append((label, int(b)))
                else: hashMap[hashVal][indexOf] = (label, b)
            elif "-" in part:
                part = part.split("-")[0]
                hashVal = hashString(part)
                hashMap[hashVal] = [(i, j) for (i, j) in hashMap[hashVal] if i != part]
            
    ans = 0
    for i in range(0, 256):
        ans += sum((i + 1) * (b + 1) * int(item[1]) for b, item in enumerate(hashMap[i]))
    return ans

def hashString(s):
    val = 0
    for c in s:
        if c == "\n": continue
        val += ord(c)
        val *= 17
        val %= 256
    return val

if __name__ == "__main__":
    print(f"The answer is {main()}")