import cv2
import numpy as np

while True:
    frame = cv2.imread('g.jpg')
    img=cv2.resize(frame,(700,512))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_b = np.array([110,50,50])
    u_b = np.array([130,255,255])
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()
        