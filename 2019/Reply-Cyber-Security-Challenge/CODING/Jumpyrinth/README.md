# Jumpyrinth

## Problem

> While doing his mission preparation tests, R-boy notices in the file he's reading that the data has been inserted in a mysterious order. Read the text with him and discover what's behind it.

[jumpyrinth.zip](jumpyrinth.zip)

## Solution

After extracting the ZIP file provided, we get 2 `.txt` files: `RULES.txt` and a file with weird symbols. The contents of `RULES.txt` are not completely clear but they seems to be some instructions on traversing a path and storing some characters in a `FLAG` string using a stack.

Since `RULES.txt` indicates that the weird characters represent some kind of labyrinth, we can proceed to rename the text file containing them to `maze.txt`. Moving on, we notice that the `$` character is supposed to represent the start of the path. However, there are several of these in our maze. Therefore, we guessed that there were several strings hidden in the maze, and we assumed that one of them would be the flag.

Given the flag format for the CTF (`{FLG:<flag>}`), we wrote a Python script to find the flag.

[Python script](solver.py)
