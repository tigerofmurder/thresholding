import cv2
import numpy as np
from matplotlib import pyplot as plt


imgc= cv2.imread('thresh3.png')
img = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)

cv2.imshow('Coverted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.axis("on")
plt.hist(img.ravel(),256,[0,256])
plt.show()

height, width = img.shape


print(height,width)

value_thr = 195#185#120
value_default = 210#187#175

for y in range(0,width):
    for x in range(0,height):
        if (value_thr <= img[x,y] and img[x,y] <= value_default):
            img[x,y] = 0

        else:
            img[x,y] = 255

cv2.imshow('Coverted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
