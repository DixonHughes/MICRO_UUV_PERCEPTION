import cv2
import numpy as np

#load data in saved order as a list 

img_list = []
for s in range(4):          #loads the saved frames from 0-4 
    for i in range(400):    #loads the image in the row of pixels in the image from 0-399
        gradians = np.load("/home/wrc/Desktop/Github/MICRO_UUV_PERCEPTION/DF8_2/"+str(s)+"_"+str(i)+".npy" )
        img_list.append(gradians)

print(len(img_list))
#stacks the output array for image construction
#out_arr = np.stack((out_list), axis = 0)

# make sure to run the following command
        # export QT_QPA_PLATFORM=xcb
img = np.zeros((400,1200,3), dtype = np.uint8)       #lines 16-20 create a black background to display returns on
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to grayscale
#cv2.imshow('gray',gray_image)
#cv2.waitKey()

#display the now saved data like the recorded video
#for s in range (4):
for j in range(1,4):
    for i in range(400):
        gray_image[i] = img_list[i*j]
        cv2. imshow('new',gray_image)
        cv2.waitKey(1)                  #allows the full image to construct before closure
