# Perfect XOR

## Problem

> Can you decrypt the flag?<br><br>
Download the file below.

[decrypt.py](decrypt.py)

## Solution

We are given some Python code. If we run it, we can see that the flag is being printed, but it's awfully slow.

```console
> ./decrypt.py
flag{tHE_
```

Looking at the code, we see that the `end` and `flush` arguments of `print()` are used to gradually print the flag without new lines appearing at every call of `print()`. We see that the next character is appended if `a(n)` returns `True`.

Examining `a(n)`, we see that it takes an integer, `n`, and loops through all positive integers below it. If `n` is divisible by the current integer, `i`, `b` is incremented by the value of `i`. Finally, the function returns `True` if `b` is equal to `n`.

So, `a()` checks if the sum of the positive divisors of an integer is equal to the value of the integer. It is checking if `n` is a [perfect number](https://en.wikipedia.org/wiki/Perfect_number).

We can speed up the printing of the flag by manually supplying a list of perfect numbers, instead of relying on `a()` to find them.

[solver.py](solver.py)