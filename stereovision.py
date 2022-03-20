from email.errors import InvalidMultipartContentTransferEncodingDefect
import matplotlib.pyplot as plt
from PIL import Image
class stereo():
    def __init__(self,imleft,imright,dmax=15) -> None:
        self.iml=imleft 
        self.imr=imright 
        self.dmax=dmax
    def show():
        plt.subplot(1,2,1)

iml=Image.open('tsukubal.png')
        