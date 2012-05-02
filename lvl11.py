from PIL import Image

im = Image.open('cave.jpg')
new_image = Image.new('RGB', (320,240))
for i in range(0,im.size[0],2):
	for j in range(0,im.size[1],2):
		new_image.putpixel((i//2,j//2), im.getpixel((i,j)))
new_image.show()
