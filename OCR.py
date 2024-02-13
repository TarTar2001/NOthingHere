import cv2 
import pytesseract

#file_path = "Sample_Car_Picture\car_14.jpg"
#file_path = "thaitextexample.jpg"
file_path = "Result_image/licenesplate_No_1.jpg"
#file_path = "Nameplate_No_1.jpg"

img = cv2.imread(filename=file_path)

# Adding custom options
custom_config = r'--oem 3 --psm 6'


#gray scale
img2 = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)

#BLUR
img3 = cv2.medianBlur(src=img2,ksize=3)

#thresholding
img4 = cv2.threshold(src=img3,thresh=0,maxval=255,type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


cv2.imshow(winname="image",mat=img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

language_thai = 'tha'
text = pytesseract.image_to_string(img,lang=None, config=custom_config)
box = pytesseract.image_to_boxes(img,lang=None, config=custom_config)
print("ocr result : ")
print(text)
print(box)
txtfile = open(file='text.txt',mode='w',encoding=None,)
txtfile.write(text)
txtfile.close()


