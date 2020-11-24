import cv2

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
img2 = img.copy()
img2[200:400, 200:400] = cv2.add(img2[200:400, 200:400], 50)
cv2.imwrite('lenna_50.bmp', img2)