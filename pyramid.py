import cv2
img=cv2.imread('dp.jpg')
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
cv2.imshow('img',img)
cv2.imshow('img',lr1)
cv2.imshow('img',lr2)
cv2.waitKey(0)
cv2.destroyAllWindows()
