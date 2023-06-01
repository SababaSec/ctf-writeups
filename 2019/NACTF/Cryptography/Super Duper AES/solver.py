#!/usr/bin/env python2
from binascii import hexlify


def substitute(hex_block):
    substituted_hex_block = ''
    # substitution = [8, 4, 15, 9, 3, 14, 6, 2, 13, 1, 7, 5, 12, 10, 11, 0]
    substitution = [15, 9, 7, 4, 1, 11, 6, 10, 0, 3, 13, 14, 12, 8, 5, 2]
    for hex_digit in hex_block:
        new_digit = substitution[int(hex_digit, 16)]
        substituted_hex_block += hex(new_digit)[2:]
    return substituted_hex_block


def pad(message):
    num_bytes = 4 - (len(message) % 4)
    return message + num_bytes * chr(num_bytes)


def hexpad(hex_block):
    num_zeros = 8 - len(hex_block)
    return num_zeros * '0' + hex_block


def permute(hex_block):
    # permutation = [
    #     6, 22, 30, 18, 29, 4, 23, 19, 15, 1, 31, 11, 28, 14, 25, 2, 27, 12, 21, 26, 10, 16, 0, 24, 7, 5, 3, 20, 13, 9, 17, 8
    # ]
    permutation = [
        22, 9, 15, 26, 5, 25, 0, 24, 31, 29, 20, 11, 17, 28, 13, 8, 21, 30, 3, 7, 27, 18, 1, 6, 23, 14, 19, 16, 12, 4, 2, 10
    ]
    block = int(hex_block, 16)
    permuted_block = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permuted_block |= bit << permutation[i]
    return hexpad(hex(permuted_block)[2:])


def round(hex_message):
    num_blocks = len(hex_message) // 8
    permuted_hex_message = ''
    for i in range(num_blocks):
        permuted_hex_message += permute(hex_message[8 * i: 8 * i + 8])
    substituted_hex_message = ''
    for i in range(num_blocks):
        substituted_hex_message += substitute(
            permuted_hex_message[8 * i: 8 * i + 8]
        )
    return substituted_hex_message


hex_message = 'd59fd3f37182486a44231de4713131d20324fbfe80e91ae48658ba707cb84841972305fc3e0111c753733cf2'

for i in range(10000):
    hex_message = round(hex_message)

print(hex_message.decode('hex'))
