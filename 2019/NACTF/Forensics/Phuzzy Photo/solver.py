from PIL import Image

IMAGE_FILE = 'pic.png'

im = Image.open(IMAGE_FILE)
out = Image.new('I', im.size) # Image.new(mode, size, color=0): mode here is 'I' which has 32-bit signed integer pixels. The default image color is black so it will be initialized to that.

width, height = im.size

for x in range(width):
    for y in range(height):
        r, g, b, _ = im.getpixel((x, y))
        if y % 6 == 0 and x % 6 == 0 and (r < 255 or g < 255 or b < 255):
            out.putpixel((x, y), 0xffffff)

out.save('new_pic.png')
