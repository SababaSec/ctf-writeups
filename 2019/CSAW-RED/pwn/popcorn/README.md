# popcorn

## Problem

> We love POPcorn<br>

[popcorn](popcorn)

[libc.so.6](libc.so.6)

## Solution

In this challenge, we are given a dynamically-linked binary and the C Standard Library shared object on the server which the binary is hosted on. Also, the challenge description hints on the fact that we need to use a `pop` ROP gadget, which we can get using [ROPgadget](https://github.com/JonathanSalwan/ROPgadget).

To pwn this binary, we need to deliver 2 stack overflow payloads. Since it is a 64-bit binary, we need to use the `rdi` register whenever we want to pass an argument to a function. We can use the `pop rdi` ROP gadget, which pops a value from the stack and inserts it into `rdi`, to achieve this.

When we are prompted for input, we deliver a stack overflow and override the instruction pointer (RIP) with the `pop rdi` address. The next value in our payload would be the GOT address of the `puts()` argument. This will then be popped into `rdi` and become our argument. Since the `pop rdi` ROP gadget is followed by `ret;` (return), execution will resume on the stack. The next value we pass is the function we want to call, in this case `puts()`, therefore we pass its Procedure Linkage Table (PLT) value. Finally, we supply the address of main as our return address. This payload results in calling the `puts()` function in order to print the GOT address of `puts()`, and then recursively calling `main()`. Therefore, the program flow repeats from the beginning.

Now that we have leaked the GOT value of `puts()`, and since we can find out the offset of `puts()` in the C Standard Library shared object given to us, we can proceed to calculate the base address of libc. When we have that, we can then obtain the address of the `system()` function in libc, as well as the address where the string `/bin/sh` appears in libc.

When we are prompted again for input, we deliver another stack overflow. This time, we use the `pop rdi` gadget to store the address of `/bin/sh` in the `rdi` register. We then call system, with `/bin/sh` as the argument. We do not need to override the return address.

[Python script](solver.py)