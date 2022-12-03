import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("haikyuu.jpg",0)
plt.hist(image.ravel(),256,[0,256])
h_eq = cv2.equalizeHist(image)
cv2.imshow("Imagem Original",image)
plt.show()

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()