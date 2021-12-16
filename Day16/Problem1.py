def readPacket(hexString = None, binaryString = None):
    if hexString is None and binaryString is None: return

    if hexString is not None:
        print(f"Decoding: {hexString}")
        binaryString = ""
        for char in hexString:
            binaryString = binaryString + bin(int(char, 16))[2:].zfill(4)
    else:
        print(f"Decoding: {binaryString}")

    packetVersion = int(binaryString[:3], 2)
    binaryString = binaryString[3:]
    packetType = int(binaryString[:3], 2)
    binaryString = binaryString[3:]

    print(f"Version: {packetVersion}, Type: {packetType}")

    if all([bit == "0" for bit in binaryString]): return 0, ""

    if packetType == 4:
        data = ""
        lastPacket = False
        while not lastPacket:
            thisPacket = binaryString[:5]
            binaryString = binaryString[5:]
            if thisPacket[0] == "0": lastPacket = True
            data = data + thisPacket[1:]
        data = int(data, 2)
        print(f"Packet value: {data}")
        return packetVersion, binaryString
    else:
        if binaryString[0]=="0": 
            binaryString = binaryString[1:]
            lengthTypeID = int(binaryString[:15], 2)
            binaryString = binaryString[15:]
            unreadBits = binaryString[lengthTypeID:]
            binaryString = binaryString[:lengthTypeID]
            print(f"Total subpacket length: {lengthTypeID}")
            print(f"Packet data: {binaryString}")

            versionSum = packetVersion
            while binaryString != "":
                version, binaryString = readPacket(binaryString=binaryString)
                versionSum += version
            
            return versionSum, unreadBits
        else:
            binaryString = binaryString[1:]
            lengthTypeID = int(binaryString[:11], 2)
            binaryString = binaryString[11:]

            print(f"Number of subpackets: {lengthTypeID}")
            versionSum = packetVersion
            for i in range(0, lengthTypeID):
                version, binaryString = readPacket(binaryString=binaryString)
                versionSum += version
            return versionSum, binaryString

with open("input.txt", "r") as file:
    hexString = file.readline()[:-1]

answer = readPacket(hexString = hexString)[0]
print(f"The answer is {answer}")