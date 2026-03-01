# Seashore

## Problem

> Sally seems super sad. Set up a solution.<br>
`nc pwn.chal.csaw.io 1003`

[seashore](seashore)

## Solution

Running [`checksec`](https://en.kali.tools/all/?tool=206) on the binary shows that the NX (no-execute) bit is off, which means that we are allowed to execute code on the stack. So, we can use a stack overflow to inject shellcode that will execute `execve("/bin/sh")`.

[Python script](solver.py)
