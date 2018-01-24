# resize pokeGAN.py
import os
import cv2
from PIL import Image

src = "./data" #pokeRGB_black
dst = "./resizedData" # resized

# os.mkdir(dst)
new_size = 160

i = 0
for each in os.listdir(src):
    # img = cv2.imread(os.path.join(src,each))
    # img = cv2.resize(img,(256,256))
    # cv2.imwrite(os.path.join(dst,each), img)
    im = Image.open(os.path.join(src,each))
    im.thumbnail((new_size, new_size))
    w, h = im.size
    bg = Image.new('RGBA', (new_size, new_size), (255, 255, 255, 255))
    bg.paste(im, ((new_size - w) // 2, (new_size - h) // 2), im)
    bg = bg.convert('RGB')
    bg.save(os.path.join(dst,str(i) + '.jpg'))

    i += 1

    # bg.show()
    