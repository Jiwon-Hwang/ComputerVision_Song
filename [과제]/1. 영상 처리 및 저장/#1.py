import cv2

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
img2 = img.copy()
img2[200:400, 200:400] += 20
cv2.imwrite('lenna_20.bmp', img2)