#Generate a 250x500 image using numpy and perform the following tasks.
#i)Draw a square , line and circle next to each other at the center of the image in a row.
#ii) Print text at button of image.
#iii) Draw a polygon with all 4 corners and center as points.
#(please refer to the result folder to check the sample image. And create a replica of it).

import cv2
import numpy as np 

img=np.zeros((250,500,3))

img=cv2.rectangle(img,(10,100),(100,155),(255,0,0),-1)

img=cv2.line(img,(110,125),(400,125),(0,0,255),3)
               
img=cv2.circle(img,(450,125),40,(0,255,0),-1)

pts=np.array([[0,0],[500,0],[0,250],[500,250]],np.int32)
img=cv2.polylines(img,[pts],True,(0,255,255),4)

font=cv2.FONT_HERSHEY_TRIPLEX
string="Skanda"
img=cv2.putText(img,string,(190,240),font,1,(255,255,200),3)

cv2.imwrite('res/assignimg.jpg',img)
cv2.imshow("Imageeeee",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
