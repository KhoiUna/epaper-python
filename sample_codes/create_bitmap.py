import qrcode
from PIL import Image
import os


def create_bitmap(url, file_name):

    img = qrcode.make(url)

    img.save(file_name + ".png")

    Image.open(file_name + ".png").save(file_name + ".bmp")

    os.remove(file_name + ".png")


# Eg: create_bitmap('una.edu', 'una')
