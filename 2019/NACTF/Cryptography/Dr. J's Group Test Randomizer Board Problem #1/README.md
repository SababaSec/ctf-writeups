# Dr. J's Group Test Randomizer: Board Problem #1

## Problem

> Dr. J is back with another group test, and he patched his prng so we can't predict the next number based on the previous one! Can still you help Leaf predict the next output of the prng?<br>
`nc shell.2019.nactf.com 31258`

[rand.c](rand.c)

## Hints

> - So we can't use the output to predict the next number... but I wonder if the numbers will repeat?

## Solution

Our task is to be able to predict the next number for a random number generator which is based on the [middle-square method](https://en.wikipedia.org/wiki/Middle-square_method). Normally, this is trivial since the previous number is the seed for the next random number. However, the implementation here is different since the digits used for the current random number and for the seed to calculate the next one are different.

Somewhere in the Wikipedia article, there is an important detail which we can use to our advantage:
> If the middle *n* digits are all zeroes, the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this method to be of practical use.

Due to the implementation difference, it is possible that the current random number is `0` but the seed is not `0`. However, if we keep on trying, at some point the seed will become `0`, and we can successfully predict the next random number to be `0`.

[Python script](solver.py)
