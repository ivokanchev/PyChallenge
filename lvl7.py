from PIL import Image
import re

im =Image.open("oxygen.png")
y = im.size[1] / 2
pixel_list = []
answer = ''
for x in range(0, im.size[0], 7):
    if ( im.getpixel((x,y))[0] == im.getpixel((x,y))[1] and
         im.getpixel((x,y))[0] == im.getpixel((x,y))[2]):
        pixel_list.append(chr(im.getpixel((x,y))[0]))
answer += ''.join(pixel_list).partition('[')[1]
answer += ''.join(pixel_list).partition('[')[2]

for char in eval(answer):
    print(chr(char), end='')

