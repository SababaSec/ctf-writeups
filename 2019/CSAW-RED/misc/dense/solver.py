#!/usr/bin/env python3
import re

with open('message.txt', 'r') as f:
    table = {
        ('00', '+', '11'): '00',
        ('00', '-', '11'): '10',
        ('10', '+', '01'): '01',
        ('10', '-', '01'): '11'
    }
    lines = f.readlines()
    lines.pop(0)
    binary = ''
    for line in lines:
        b1, b2 = re.findall('[0-9]{2}', line)
        o = re.search('[-+]', line).group(0)
        binary += table[(b1, o, b2)]

    print(''.join(chr(int(binary[i*8:i*8+8], 2)) for i in range(len(binary) // 8)))
