import numpy
import cv2
#define original image with path
path = r'C:\Users\rory5\OneDrive\Desktop\code\PYTHON\house.tiff'
#read image
original_image = cv2.imread(path)
#create the box blur kernel and operation
#def boxblur

#show user images
cv2.imshow("Original", original_image)
#cv2.imshow("Blurred", edited_image)

#close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
