import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('V&P.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.waitKey(0)