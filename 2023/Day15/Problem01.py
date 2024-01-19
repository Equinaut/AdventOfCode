def main():
    ans = 0
    with open("input.txt") as file:
        contents = file.read()
        parts = contents.split(",")
        ans += sum(map(hashString, parts))
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