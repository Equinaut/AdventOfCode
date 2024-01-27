# False represents low pulse
# True represents high pulse

# Pulse type is a tuple
# (Origin, Destination, PulseType)

from math import lcm

def main():
    allNodes = []    
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

    for i in sendsTo: allNodes.append(i)

    sendsToRx = []
    for i in sendsTo:
        if "rx" in sendsTo[i]: sendsToRx.append(i)
    sendsToRx2 = dict()
    for i in sendsTo:
        if any(a in sendsTo[i] for a in sendsToRx): sendsToRx2[i] = None
    # sendsToRx2 all need to a highpulse
    # This will trigger sendsToRx to send a low pulse

    i = 0
    while None in sendsToRx2.values():
        i += 1
        sent = pressButton(sendsToRx2, sendsTo, flipFlipStates, conjunctionStates)
        if sent:
            for j in sent: sendsToRx2[j] = i

    return lcm(*sendsToRx2.values())

def pressButton(watching, sendsTo, flipFlipStates, conjunctionStates):
    pulseQueue = [("button", "broadcaster", False)]
    sent = []

    while pulseQueue:
        newPulse = pulseQueue.pop(0)
        newPulses = sendPulse(newPulse, sendsTo, flipFlipStates, conjunctionStates)
        pulseQueue.extend(newPulses) 

        if newPulse[0] in watching and newPulse[2]:
            sent.append(newPulse[0])

    return sent


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