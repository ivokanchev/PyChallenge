from PIL import Image


def spiral(X, Y):   
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            #if X//2 + x >= 100 or Y//2 + y >= 100:
                #print (X//2 + x, Y//2 + y)
            doS((X//2 + x, Y//2 + y), new, img.getpixel((9999-i,0)))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy


def doS(coords, pic, value):
    pic.putpixel(coords, value)

img = Image.open('wire.png')
new = Image.new('RGB', (101,101), (0,0,0))
spiral(100, 100)
new.show()
