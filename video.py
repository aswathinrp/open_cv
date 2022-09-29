import cv2
import datetime
cap=cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 700)
cap.set(4,700)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        text= 'width' + str(cap.get(3)) + 'height' + str(cap.get(4))
        datet=str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_COMPLEX
        frame = cv2.putText(frame,datet,(0,100),font,1,(0,255,0),2)
        
    
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()        