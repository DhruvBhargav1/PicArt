#fixing the imports
import cv2
import numpy as np

#..........phase1
#reading the img
image = cv2.imread('test1.jpg')

#resizing the image
#interpolation is cubic for best result
image_resized= cv2.resize(image,None,fx=1,fy=1)

#..........phase2
#removing impurities
image_cleared=cv2.medianBlur(image_resized,3)
image_cleared=cv2.medianBlur(image_cleared,3)
image_cleared=cv2.medianBlur(image_cleared,3)

image_cleared=cv2.edgePreservingFilter(image_cleared,sigma_s=5)

#.......phase3
#Bilateral Image filtering
image_filtered=cv2.bilateralFilter(image_cleared,3,10,5)
#cv2.bilateralFilter(src,d,sigmacolor,sigmaspace)

for i in range(2):
    image_filtered=cv2.bilateralFilter(image_filtered,3,20,10)

for i in range(3):
    image_filtered=cv2.bilateralFilter(image_filtered,3,30,10)


#..........phase4
#sharpening the image using addweighted()
gaussian_mask=cv2.GaussianBlur(image_filtered,(7,7),2)
image_sharp=cv2.addWeighted(image_filtered,1.5,gaussian_mask,-0.5,0)
image_sharp=cv2.addWeighted(image_sharp,1.4,gaussian_mask,-0.2,10)

#displaying image
cv2.imshow('final Image',image_sharp)
cv2.imshow('clear Impurities',image_cleared)
cv2.imshow('original',image_resized)
#cv2.imwrite('jpg file',image_sharp)
cv2.waitKey(0)