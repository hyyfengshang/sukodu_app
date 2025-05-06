import os

from PIL import Image

imagePath = r"E:\test\OIP-C.jfif" #读入文件名称

outputPath = os.path.join(os.path.dirname(imagePath), os.path.basename(imagePath).split('.')[0] + '.webp')
im = Image.open(imagePath) #读入文件
im.save(outputPath) #编码保存