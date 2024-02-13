import cv2
import numpy as np
path = 'Sample_Car_Picture/car_02.jpg'
nplateCascadeclassifier = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
count = 0
minArea = 1000


task = cv2.imread(path)
imgGray = cv2.cvtColor(task, cv2.COLOR_BGR2GRAY)
numplate = nplateCascadeclassifier.detectMultiScale(image           = imgGray, 
                                                    scaleFactor     = 1.1, 
                                                    minNeighbors    = 4         )


print(numplate)
for (x,y,w,h) in numplate:
    print("start point == "+str(x)+","+str(y))
    print("width == "+str(w) )
    print("hight == "+str(h))
    area = w*h
    if area > minArea:
        #cv2.rectangle(task,(x,y),(x+w,y+h),(0,0,255),2)
        
        cv2.putText(task," ",(x,y-35),cv2.FONT_HERSHEY_PLAIN,2.5,(0,255,0),2)
        imgRoi = task[y:y+h,x:x+w]
        cv2.imshow("ROI",imgRoi)
        cv2.imshow("Original",task)
        
if cv2.waitKey(0) & 0xFF == ord('s'):
        cv2.imwrite("Result_image/licenesplate_No_1.jpg",imgRoi) 
        cv2.putText(task,"save",(50,50),cv2.FONT_HERSHEY_PLAIN,2.5,(0,255,0),2)
 
        cv2.imshow("saved",task)
        #cv2.waitKey(500)
        print("press [[ s ]] to save image")