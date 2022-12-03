import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("haikyuu.jpg")
color = ('b','g','r')

for i, col in enumerate(color):
    print(i,col)
    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])

cv2.imshow("Imagem original",image)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()