import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
cv.imshow("blank",blank)
# paint the image a color
blue=255,0,0
green=0,255,0
red=0,0,255
#blank[200:300,300:400]=blue
#cv.imshow("color",blank)
# draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),green,thickness=-1)
cv.imshow("rectangle",blank)
#draw a circle
cv.circle(blank,(250,250),40,red,-1)
cv.imshow("circle",blank)
cv.waitKey(0) 