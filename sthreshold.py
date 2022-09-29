import cv2

img=cv2.imread('g.jpg',0)
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th3',th3)
print(cv2.imshow('th1',img))

cv2.waitKey()
cv2.destroyAllWindows()
