import os
import pyqrcode

cw = os.getcwd()
os.chdir(cw)

def generate(link):
    url = pyqrcode.create(link)
    url.png("myqr.png", scale=5)