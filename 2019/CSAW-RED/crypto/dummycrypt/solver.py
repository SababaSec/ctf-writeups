#!/usr/bin/env python2
text = 'Hellothere everybody how are you doing today_long-plaintexts-are fun'
cipherText = '2c4f4b5168535a574f57064853485e5b3f5c4856124e525402406942076b60521156565358440057615644693c5e554d530a605d4064525e445d6d521f534f5706495251'

def decrypt(text, cipherText):
    cipherText = cipherText.decode('hex')
    key = ''
    for i in range(len(text)):
        plain = ord(text[i])
        cipher = ord(cipherText[i]) + 65
        key += chr(cipher - plain + 65)
        if key[-1] == '}':
            break
    print(key)

decrypt(text, cipherText)
