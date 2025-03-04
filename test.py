import numpy as np
##pip install opencv-python
import cv2 as cv

##read image from path
myimg = cv.imread("C:\\Users\\longp\\Downloads\\WIN_20240124_19_23_42_Pro.jpg")

##remove color blue
##0 : blue, 1: green , 2 : red
myimg[:,:,0] = 0

print(myimg.shape)

cv.imshow("image", myimg)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv.destroyAllWindows()