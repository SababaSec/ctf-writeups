#!/usr/bin/env python3
from PIL import Image


im = Image.open('pic.png')
out = Image.new('I', im.size, 0)

width, height = im.size
for x in range(width):
    for y in range(height):
        r, g, b, _ = im.getpixel((x, y))
        if y % 6 == 0 and x % 6 == 0 and (r < 255 or g < 255 or b < 255):
            out.putpixel((x, y), 0xffffff)

out.save('pic2.png')
