from PIL import Image

a = [[],[],[],[],[]]

formats = ['PNG', 'GIF', 'JFIF']

with open('evil2.gfx', 'rb') as evil:
    [ a[i%5].append(str(char)) for i, char in enumerate(evil.read()) ]

for img in range(len(a)):
    for imgFormat in formats:
        if (''.join([chr(int(x)) for x in a[img][:10]]).find(imgFormat)) != -1:
            imgName = 'img' + str(img) + '.' + imgFormat.lower()
            with open(imgName, 'wb') as image:
                image.write(bytes([int(char) for char in a[img]]))
