import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
import os

filename_0 = r'C:\Users\Juliana\Downloads\radiografia_crop3.jpg'
img_0 = cv2.imread(filename_0)

img_1 = cv2.cvtColor(img_0,6)

img_2 = cv2.equalizeHist(img_1)

retval, img_3 = cv2.threshold(img_2,125,255,8)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))

img_4 = cv2.morphologyEx(img_3,2,kernel)

img_5 = cv2.Canny(img_4,100,200,3)

cv2.imshow('Imagen Resultado', img_5)
cv2.waitKey(0)

directory = r'C:\Users\Juliana\Downloads'

os.chdir(directory)
img_1 = cv2.imwrite('color.jpg', img_1)
img_2 = cv2.imwrite('eqhist.jpg', img_2)
img_3 = cv2.imwrite('otsu.jpg', img_3)
img_4 = cv2.imwrite('open.jpg', img_4)
img_5 = cv2.imwrite('canny.jpg', img_5)


