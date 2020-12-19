import numpy as np
from zipfile import ZipFile
from PIL import Image

# https://stackoverflow.com/questions/33166316/how-to-read-an-image-inside-a-zip-file-with-pil-pillow

filename = 
with ZipFile(filename) as archive:
    for entry in archive.infolist():
        with archive.open(entry) as file:
            img = Image.open(file)
            print(img.size, img.mode, len(img.getdata()))
