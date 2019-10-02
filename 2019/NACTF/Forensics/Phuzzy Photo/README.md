# Phuzzy Photo

## Problem

> Joyce's friend just sent her this photo, but it's really fuzzy. She has no idea what the message says but she thinks she can make out some black text in the middle. She gave the photo to Oligar, but even his super eyes couldn't read the text. Maybe you can write some code to find the message?<br>
Also, you might have to look at your screen from an angle to see the blurry hidden text<br>
P.S. Joyce's friend said that part of the message is hidden in every 6th pixel

[pic.png](pic.png)

## Solution

We extract every 6th pixel from the image if it is not white.

[Python script](solver.py)
