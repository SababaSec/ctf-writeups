# Seashore

## Problem

> Sally seems super sad, set up a solution<br>
`nc pwn.chal.csaw.io 1003`

[seashore](seashore)

## Solution

Running [`checksec`](https://en.kali.tools/all/?tool=206) on the binary shows that the NX bit (no-execute) is turned off, which means that we are allowed to execute code on the stack. So, we can use a stack overflow to inject shellcode which will run `execve("/bin/sh")`.

[Python script](solver.py)