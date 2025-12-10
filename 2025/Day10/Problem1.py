
def solveCase(lights, buttons):
    # List of reachable configurations, gets expanded on each pass
    reachable = { lights, }
    ans = 0
    while True:
        new = set()
        for v in reachable:
            for b in buttons:
                # if v == b, then this button can be pressed on the next go to toggle all of the lights
                if v == b: return ans + 1
                new.add(v ^ b)
        reachable = new
        ans += 1

def main():
    ans = 0
    machines = []
    with open("input.txt") as file:
        for line in file:
            lights = None
            buttons = []
            for section in line[:-1].split(" "):
                if section[0] == "[": lights = int(section[1:-1][::-1].replace(".", "0").replace("#", "1"), base=2)
                elif section[0] == "(":
                    v = 0
                    for b in section[1:-1].split(","): v |= 1 << int(b)
                    buttons.append(v)
            machines.append((lights, tuple(buttons)))
        
    # Solve each case and sum the results
    for i, (lights, buttons) in enumerate(machines):
        ans += solveCase(lights, buttons)
        print(f"({i} / {len(machines)}) - {ans} \t {bin(lights)[2:]}")
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
