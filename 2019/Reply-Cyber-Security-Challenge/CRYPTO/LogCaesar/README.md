# LogCaesar

## Problem

> The satellite communications have stopped working – suddenly they're sending back unknown algorithms. Help R-boy decipher them.

[encrypt.py](encrypt.py)

[encrypted.txt](encrypted.txt)

## Solution

We are given 2 things, some ciphertext and the code which was used to encrypt it.

Since we are given the encrypt function, we can go ahead and reverse it. The problem is that we do not know the 256-digit key that was used for the encryption.

However, not knowing the 256-digit key turns out not to be a problem due to the line `new_pos = (3**(key+i)) % 257`. The key is used to generate a new position by generating a value based on powers of 3. For all the possible values of the 256-digit key, there are only 256 possible outputs. Moreover, since 3 is a [primitive root](https://en.wikipedia.org/wiki/Primitive_root_modulo_n) modulo 257 (they are coprime), this would result in a cyclic sequence. The only variable that determines the ciphertext, apart from the plaintext itself, is the starting point of the sequence, which is a number from `1` to `257` (which translates to an array index from `0` to `256` due to the use of `ciphertext[new_pos-1]`). This number becomes our actual key, and we are able to brute-force it until we find a flag in our required format, `{FLG:<flag>}`).

[Python script](solver.py)
