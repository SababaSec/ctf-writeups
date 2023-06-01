#!/usr/bin/env python3
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
target = 0x1371fcaacf98


def get_value(char):
    value = ord(char)
    if value < 0x3a:
        value += 0x4
    elif value < 0x5b:
        value -= 0x41
    else:
        value -= 0x47
    return value


def get_flag():
    flag = ''
    total = 0
    for i in range(8):
        total *= 0x3e
        prev = ''
        for c in chars:
            if (total + get_value(c)) * 0x3e ** (7 - i) > target:
                break
            prev = c
        flag += prev
        total += get_value(prev)

    print('nactf{' + flag + '}')


get_flag()
