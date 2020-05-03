#!/usr/bin/env python3
import sys

if len(sys.argv) != 4:
    print("Usage: "+sys.argv[0]+" message_file key encrypted")
    sys.exit(1)

def encrypt(message, key):
    with open(message, 'rb') as content_file:
        content = content_file.read()
    if len(content) != 256:
        raise Exception('This is a block cipher, messages have to be exactly 256 bytes long')
    ciphertext = list(' ' * 256)
    for i in range(0,256):
        new_pos = (3**(key+i)) % 257
        ciphertext[new_pos-1] = ((content[i])^i)^(new_pos-1)
    return bytes(ciphertext)

ciphertext = encrypt(sys.argv[1],int(sys.argv[2]))
with open(sys.argv[3],'wb') as encryped_file:
    encryped_file.write(ciphertext)


