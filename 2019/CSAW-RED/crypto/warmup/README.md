# warmup

## Problem

> Let's start off with the basics:<br>
`0f05080e1220360106190c3610061c360207061e361e01081d4e1a2e0600070e362607210c1b0c4814`

## Solution

This is an XOR cipher with key length 1. As the challenge title implies, this is easy to crack. All we have to do is unhexlify the ciphertext and then try to XOR that with all possible ASCII characters until we find the key which results in the flag.

[Python script](solver.py)
