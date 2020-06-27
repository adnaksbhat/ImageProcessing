# Create an image using numpy. 
# Draw a rectangle of red and also do one more with blue and green.
# Create a video of 120sec with these 3 images with 1 FPS. Save, upload and send the drive link via assignment 3 form. 


import numpy as np
import cv2
import matplotlib.pyplot as plt

red=np.zeros((200,500,3))
blue=np.zeros((200,500,3))
green=np.zeros((200,500,3))


red=cv2.rectangle(red,(100,75),(200,125),(0,0,255),5)
green=cv2.rectangle(green,(200,75),(300,125),(0,255,0),5)
blue=cv2.rectangle(blue,(300,75),(400,125),(255,0,0),5)

# cv2.imwrite('res/redrectangle.jpg',red)
# cv2.imwrite('res/bluerectangle.jpg',blue)
# cv2.imwrite('res/greenrectangle.jpg',green)


fcc=cv2.VideoWriter_fourcc('X','V','I','D')
output=cv2.VideoWriter('result/del.avi',fcc,1.0,(500,200))

redimg=cv2.imread("res/redrectangle.jpg")
greenimg=cv2.imread("res/greenrectangle.jpg")
blueimg=cv2.imread("res/bluerectangle.jpg")



# count=40   #red 1sec blue 1 sec green 1sec then reduce count by 1 ...so on.. so 40 times these 3 gives 120

# while (count>0):
#     output.write(redimg)
#     output.write(greenimg)
#     output.write(blueimg)
  
#     count-=1

#     if count==0:
#         break

   
    
  


# output.release()
        





# cv2.imshow("Imageeeee",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# plt.imshow(red)
# plt.show()



img_array = []
count=120
img_array.append(redimg)
img_array.append(greenimg)
img_array.append(blueimg)

while(count>0):
    for i in range(len(img_array)):
        output.write(img_array[i])
        count-=1
        if(count==0):
            break
output.release()