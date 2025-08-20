import numpy as np
import cv2

cap = cv2.VideoCapture(0)# 0-for your webcam and path to some stock video

while True:
    ret , frame = cap.read()
    height=int(cap.get(4))
    width=int(cap.get(3))
                #source image,starting pos ,end pos ,color ,line thickness
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10 )
    img = cv2.line(img,(0,height),(width,0),(0,255,0),10 )

    #rectangle               top left  bottom right   -1 for filling the rectangle instead of thickness
    img = cv2.rectangle(img,(100,100),(200,200),(0,0,255),-1)
    #circle             centre of circle as start pos
    img =cv2.circle(img,(width//2,height//2),60,(255,255,255),10)
    #text 
    font = cv2.FONT_HERSHEY_SIMPLEX      #bottom left start pos
    img=cv2.putText(img,"This is Fun!!!",(0,height//2),font,2,(255,100,100),5,cv2.LINE_AA)
    
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
