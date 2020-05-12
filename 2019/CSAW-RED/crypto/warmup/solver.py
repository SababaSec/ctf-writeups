#!/usr/bin/env python3
import binascii


str1 = binascii.unhexlify(
    '0f05080e1220360106190c3610061c360207061e361e01081d4e1a2e0600070e362607210c1b0c4814'
)

for i in range(255):
    str2 = ''
    for c in str1:
        str2 += chr(c ^ i)
    if 'flag{' in str2:
        print(str2)
