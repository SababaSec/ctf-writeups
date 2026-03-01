# Lunchtable Simulator

## Problem

> Sometimes where you sit at the table matters.<br>
`nc pwn.chal.csaw.io 1001`

[lunchtable](lunchtable)

## Solution

When we analyze the binary in `gdb`, we find that `puts()` is called to print a “goodbye” message at the end of the program. We also find a function called `system_wrapper()`, which allows us to easily call the `system()` function. The idea here is to replace the address of `puts()` with the address of `system_wrapper()`, and to replace the argument with `"/bin/sh"`.

[Python script](solver.py)
