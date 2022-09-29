import cv2
img=cv2.imread('dp.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()