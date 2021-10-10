import numpy as np
import cv2
import time

img = cv2.imread("pic.png")
pp = 0

width, height, cha = img.shape
tStart2 = time.time()
time.sleep(1)

for x in range(height):
    for y in range(width):
        for z in range(3):
            if(img[y][x][z]>=130):
                pp = pp + 1
            if(img[y][x][z]<130):
                img[y][x][z] = 0

tend2 = time.time()

cv2.imshow("pic", img)
##################################################################################

cv2.namedWindow("Original")
cv2.moveWindow("Original", 450, 250)
image = cv2.imread("pic.png")

#cv2.imshow("Original", image)
#cv2.waitKey(0)

cv2.namedWindow("Red")
cv2.moveWindow("Red", 450, 250)
cv2.namedWindow("Green")
cv2.moveWindow("Green", 450, 250)
cv2.namedWindow("Blue")
cv2.moveWindow("Blue", 450, 250)

(B, G, R) = cv2.split(image)#提取R、G、B分量
tStart1 = time.time()
time.sleep(1)

a4 = np.sum(R < 130)
a5 = np.sum(G < 130)
a6 = np.sum(B < 130)

a = np.sum(R >= 130)
b = np.sum(G >= 130)
c = np.sum(B >= 130)

aa = R[R < 130] = 0
bb = G[G < 130] = 0
cc = B[B < 130] = 0

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
#cv2.imshow("Original", image)

#print("1:",  R, "2:", G, "3:", B)
print("小於130個數:", "R:", a4, "G:", a5, "B:", a6)
print("大於等於130個數:", "R:", a, "G:",  b, "B:", c)



image = cv2.imread("pic.png")
img1 = np.array(image)

tStart1 = time.time()
time.sleep(1)
img1 = np.where(img1 < 130, 0, img1)
cv2.imshow("aaa", img1)
tend1 = time.time()

print("for耗時:", tend2 - tStart2)
print("npy耗時:", tend1 - tStart1)
cv2.waitKey(0)
