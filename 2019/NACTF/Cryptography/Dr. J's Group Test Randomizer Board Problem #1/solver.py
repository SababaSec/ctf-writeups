#!/usr/bin/env python3
from pwn import *


guessed = False


def send_zeros():
    r.recvuntil('> ')
    for _ in range(4):
        r.sendline('0')
        res = r.recv().decode('L1')
        print(res)
        if res[0] == 'T':
            return
        elif res[0:2] == 'Oh':
            guessed = True
    print(r.recv().decode('L1'))


while not guessed:
    r = remote('shell.2019.nactf.com', 31258)
    r.recvuntil('> ')
    num = 1
    while num != 0:
        r.sendline('r')
        num = int(r.recvline().strip())
        r.recvuntil('> ')
    r.sendline('g')
    send_zeros()
    r.close()
