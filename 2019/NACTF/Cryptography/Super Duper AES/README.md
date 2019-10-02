# Super Duper AES

## Problem

> The Advanced Encryption Standard (AES) has got to go. Spencer just invented the Super Duper Advanced Encryption Standard (SDAES), and it's 100% unbreakable. AES only performs up to 14 rounds of substitution and permutation, while SDAES performs 10,000. That's so secure, SDAES doesn't even use a key!

[cipher.txt](cipher.txt)

[sdaes.py](sdaes.py)

## Hints

> - Spencer used this video as inspiration for Super Duper AES: https://www.youtube.com/watch?v=DLjzI5dX8jc

## Solution

We reverse the substitution and permutation tables and the order of steps in the encryption process in order to decode the message.

[Python script](solver.py)
