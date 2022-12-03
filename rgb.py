import numpy as np
import cv2

def showImage(img):
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    obj_img = cv2.imread("V&P.jpg",0)
    print(obj_img.shape)
    showImage(obj_img)

main()

    