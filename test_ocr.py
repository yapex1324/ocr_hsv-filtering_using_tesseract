from PIL import Image
import pytesseract

import numpy as np
import cv2

while(1):
    #read source image
    img=cv2.imread("22.jpg")
    #convert sourece image to HSC color mode
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #
    hsv_low = np.array([11, 0, 0], np.uint8)
    hsv_high = np.array([162, 255, 255], np.uint8)

    #making mask for hsv range
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    # print (mask)
    
    #masking HSV value selected color becomes black
    res = cv2.bitwise_and(img, img, mask=mask)

    #show image
    cv2.imshow('mask',mask)
    cv2.imwrite("mask.jpg", mask)
    cv2.imshow('res',res)

    #waitfor the user to press escape and break the while loop 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

filename = 'mask.jpg'
img1 = Image.open(filename)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img1)
print(text)