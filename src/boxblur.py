import numpy
import cv2
from PIL import Image, ImageFilter
#define original image with path
path = r'C:\Users\rory5\OneDrive\Desktop\code\PYTHON\house.tiff'
#read image
original_image = cv2.imread(path)
#create the box blur kernel and operation
def boxblur(path, radius=1):
  img = Image.open(path).convert(RGB)
  edited_image = img.copy()
  width, height = img.size
  area = (2*radius+1)**2
  for x in range(r, width-r):
    for y in range(r, height-r):
      sum_pixels(0, 0, 0)
      
  


#show user images
cv2.imshow("Original", original_image)
#cv2.imshow("Blurred", edited_image)

#close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
