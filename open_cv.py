import time as t
import cv2
import numpy as np
path = 'Sample_Car_Picture/car_01.jpg'
nplateCascadeclassifier = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    
    task = cv2.imread(path)
    cv2.imshow('frame', frame) 
    cv2.putText(frame,"save",(50,50),cv2.FONT_HERSHEY_PLAIN,2.5,(0,255,0),2)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

    window_name = 'image'
vid.release()   
    
    
    
'''
    # Using cv2.imshow() method 
    # Displaying the image 
    cv2.imshow(window_name, task) 
    
    # waits for user to press any key 
    # (this is necessary to avoid Python kernel form crashing) 
    cv2.waitKey(0) 
    
    # closing all open windows 
    cv2.destroyAllWindows() 
'''