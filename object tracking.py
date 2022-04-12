import numpy as np
import cv2

tracker = cv2.TrackerKCF_create()
tracker2 = cv2.TrackerCSRT_create()
video = cv2.VideoCapture('street.mp4')
ok,frame = video.read()

bbox = cv2.selectROI(frame)
bbox2= cv2.selectROI(frame)

ok = tracker.init(frame,bbox)
ok2 = tracker2.init(frame,bbox)
while True :
    ok,frame = video.read()
    if not ok:
        break
    ok ,bbox= tracker.update(frame)
    ok2 ,bbox2= tracker2.update(frame)
    if ok:
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1,)
    else:
        cv2.putText(frame,'ERORR',(100,80),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,250),3)


    if ok2:
        (x,y,w,h) = [int(v) for v in bbox2]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(250,0,0),2,1,)
    else:
        cv2.putText(frame,'ERORR2',(100,80),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,250),3)

    cv2.imshow('Tracking',frame)
    if cv2.waitKey(1)& 0xFF == 27 : #Esc
        break