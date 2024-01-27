# False represents low pulse
# True represents high pulse

# Pulse type is a tuple
# (Origin, Destination, PulseType)

def main():
    sendsTo = dict()
    flipFlipStates = dict()
    conjunctionStates = dict()

    sendsTo["button"] = ["broastcaster"]

    with open("input.txt") as file:
        lines = file.readlines()

        for line in lines:
            sending = line.split(" -> ")[0]
            if sending[0] == "%":
                sendsTo[sending[1:]] = []
                flipFlipStates[sending[1:]] = False
            
            if sending[0] == "&":
                sendsTo[sending[1:]] = []
                conjunctionStates[sending[1:]] = {}

            if sending == "broadcaster":
                sendsTo["broadcaster"] = []

        for line in lines:
            sending = line.split(" -> ")[0]

            if sending[0] == "%" or sending[0] == "&": sending = sending[1:]

            receiving = line[:-1].split(" -> ")[1].split(", ")
            
            if sending in sendsTo:
                for r in receiving:
                    sendsTo[sending].append(r)
                    if r in conjunctionStates:
                        conjunctionStates[r][sending] = False

        for r in sendsTo["broadcaster"]:
            if r in conjunctionStates:
                conjunctionStates[r]["broadcaster"] = False

    highCount = 0
    lowCount = 0
    for i in range(1000):
        pulseQueue = [("button", "broadcaster", False)]
        while pulseQueue:
            newPulse = pulseQueue.pop(0)
            printPulse(newPulse)
            if newPulse[2]: highCount += 1
            else: lowCount += 1
            newPulses = sendPulse(newPulse, sendsTo, flipFlipStates, conjunctionStates)
            pulseQueue.extend(newPulses)

    ans = highCount * lowCount
    return ans

def sendPulse(pulse, sendsTo, flipFlipStates, conjunctionStates):
    origin, dest, pulseType = pulse
    
    newPulses = []

    if dest == "broadcaster":
        for nd in sendsTo["broadcaster"]:
            newPulses.append((dest, nd, pulseType))
        return newPulses

    if dest in flipFlipStates:
        if not pulseType:
            flipFlipStates[dest] = not flipFlipStates[dest]
            for nd in sendsTo[dest]:
                newPulses.append((dest, nd, flipFlipStates[dest]))

    elif dest in conjunctionStates:
        conjunctionStates[dest][origin] = pulseType
        pulseType = not all(conjunctionStates[dest].values())
        for nd in sendsTo[dest]:
            newPulses.append((dest, nd, pulseType))
    return newPulses

def printPulse(pulse):
    origin, dest, pulseType = pulse
    if pulseType: pulseType = "High"
    else: pulseType = "Low"
    print(f"{origin} -{pulseType}-> {dest}")

if __name__ == "__main__":
    print(f"The answer is {main()}")