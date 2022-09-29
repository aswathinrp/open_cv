from msilib.schema import Font
import cv2
img=cv2.imread('dp.jpg')
cv2.line(img,(0,0),(400,400),(0,255,0),5)
cv2.rectangle(img,(0,0),(200,200),(255,0,0),3)
cv2.circle(img,(100,100),50,(0,0,255),-1)
Font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"hello",(200,200),Font,3,(255,255,0),cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)