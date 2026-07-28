import cv2 as cv 
img=cv.imread("senegal-flag.jpg")
# converting to greyscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("greyscaled",gray)
cv.waitKey(0)