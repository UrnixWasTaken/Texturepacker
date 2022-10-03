from PIL import Image 
import os, sys
size = 64
image_size = 1024
path = ('C:/Users/User/Desktop/obrazki/')
dirs = os.listdir( path )
images = []
def collage():
    ele = 0
    col = Image.new("RGBA",  (image_size,image_size))
    for i in images:
       column_index =  ele % (image_size // size)
       row_index = ele // (image_size // size)
       col.paste(i,(column_index * 64, row_index * 64))
       ele += 1
    col.show()
def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResized = im.resize((size, size), Image.ANTIALIAS)
            images.append(imResized)
            print(imResized)
resize()
collage()

