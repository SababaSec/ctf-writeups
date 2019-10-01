# SafeSpace

## Problem

> We all need a little bit of wiggle room<br>
`nc pwn.chal.csaw.io 1002`

[safespace](safespace)

## Solution

We can start by finding out the list of functions present in the compiled binary. [This Stack Overflow question](https://stackoverflow.com/questions/392142/) shows various ways we can do this.

There is a function called `give_shell()`. This probably gives us a shell if we manage to call it. To do that, we can use a simple stack overflow to overwrite the 64-bit instruction pointer (RIP) with the address of `give_shell()`.

[Python script](solver.py)