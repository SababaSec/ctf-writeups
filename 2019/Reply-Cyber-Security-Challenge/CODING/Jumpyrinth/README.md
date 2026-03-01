# Jumpyrinth

## Problem

> While doing his mission preparation tests, R-boy notices in the file he’s reading that the data has been inserted in a mysterious order. Read the text with him and discover what’s behind it.

[jumpyrinth.zip](jumpyrinth.zip)

## Solution

After extracting the ZIP file provided, we get two `.txt` files: `RULES.txt` and a file containing symbols. The contents of `RULES.txt` are not straightforward, but they seem to be instructions on traversing a path and storing some characters in a `FLAG` string using a stack.

Since `RULES.txt` indicates that the weird characters represent a labyrinth, we can rename the text file containing them to `maze.txt`. Moving on, we notice that the `$` character is supposed to represent the start of the path. However, there are many of these in our maze. We guessed that there were several strings hidden in the maze, and we assumed that one of them would be the flag.

Given the flag format for the CTF, `{FLG:<flag>}`, we wrote a Python script to find the flag.

[Python script](solver.py)
