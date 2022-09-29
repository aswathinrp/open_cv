import cv2
img= cv2.imread('dp.jpg')
cv2.line(img,(0,0),(400,400),(255,0,0),5)
cv2.circle(img,(200,200),50,(0,0,255),-1)
cv2.rectangle(img,(0,0),(200,200),(0,255,0),3)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"hello",(100,100),font,4,(0,255,255),cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()