from binascii import hexlify

def substitute(hexBlock):
    substitutedHexBlock = ""
    # substitution = [8, 4, 15, 9, 3, 14, 6, 2, 13, 1, 7, 5, 12, 10, 11, 0]
    substitution = [15, 9, 7, 4, 1, 11, 6, 10, 0, 3, 13, 14, 12, 8, 5, 2]
    for hexDigit in hexBlock:
        newDigit = substitution[int(hexDigit, 16)]
        substitutedHexBlock += hex(newDigit)[2:]
    return substitutedHexBlock

def pad(message):
    numBytes = 4-(len(message)%4)
    return message + numBytes * chr(numBytes)

def hexpad(hexBlock):
    numZeros = 8 - len(hexBlock)
    return numZeros*"0" + hexBlock

def permute(hexBlock):
    # permutation = [6, 22, 30, 18, 29, 4, 23, 19, 15, 1, 31, 11, 28, 14, 25, 2, 27, 12, 21, 26, 10, 16, 0, 24, 7, 5, 3, 20, 13, 9, 17, 8]
    permutation = [22, 9, 15, 26, 5, 25, 0, 24, 31, 29, 20, 11, 17, 28, 13, 8, 21, 30, 3, 7, 27, 18, 1, 6, 23, 14, 19, 16, 12, 4, 2, 10]
    block = int(hexBlock, 16)
    permutedBlock = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permutedBlock |= bit << permutation[i]
    return hexpad(hex(permutedBlock)[2:])

def round(hexMessage):
    numBlocks = len(hexMessage)//8
    permutedHexMessage = ""
    for i in range(numBlocks):
        permutedHexMessage += permute(hexMessage[8*i:8*i+8])
    substitutedHexMessage = ""
    for i in range(numBlocks):
        substitutedHexMessage += substitute(permutedHexMessage[8*i:8*i+8])
    return substitutedHexMessage

hexMessage = 'd59fd3f37182486a44231de4713131d20324fbfe80e91ae48658ba707cb84841972305fc3e0111c753733cf2'

for i in range(10000):
    hexMessage = round(hexMessage)

print(hexMessage.decode('hex'))
