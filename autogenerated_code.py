import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt


filename_0 = r'C:\Users\trini\Pictures\image(22).jpg'
img_0 = cv2.imread(filename_0)

img_1 = cv2.medianBlur(img_0,13)

thresh, img_2 = cv2.threshold(img_1,145,255,0)

cv2.imshow('Imagen Resultado', img_2)
cv2.waitKey(0)

