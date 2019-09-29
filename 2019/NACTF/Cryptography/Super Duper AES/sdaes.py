import sys
from binascii import hexlify

def substitute(hexBlock):
    substitutedHexBlock = ""
    substitution =  [8, 4, 15, 9, 3, 14, 6, 2,
                    13, 1, 7, 5, 12, 10, 11, 0]
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
    permutation =   [6, 22, 30, 18, 29, 4, 23, 19,
                    15, 1, 31, 11, 28, 14, 25, 2,
                    27, 12, 21, 26, 10, 16, 0, 24,
                     7, 5, 3, 20, 13, 9, 17, 8]
    block = int(hexBlock, 16)
    permutedBlock = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permutedBlock |= bit << permutation[i]
    return hexpad(hex(permutedBlock)[2:])

def round(hexMessage):
    numBlocks = len(hexMessage)//8
    substitutedHexMessage = ""
    for i in range(numBlocks):
        substitutedHexMessage += substitute(hexMessage[8*i:8*i+8])
    permutedHexMessage = ""
    for i in range(numBlocks):
        permutedHexMessage += permute(substitutedHexMessage[8*i:8*i+8])
    return permutedHexMessage



if __name__ == "__main__":
    hexMessage = str(hexlify(str.encode(pad(sys.argv[1]))))
    if "\'" in hexMessage:
        hexMessage = hexMessage[2:-1]

    for i in range(10000):
        hexMessage = round(hexMessage)
    print (hexMessage)
