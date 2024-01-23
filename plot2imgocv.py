import cv2
import matplotlib.pyplot as plt
import numpy as np

# make sure to rurnt the following command
# export QT_QPA_PLATFORM=xcb

img = np.zeros((400,400,3), dtype = np.uint8)       #lines 17-19 create a black background to display returns on

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to grayscale
cv2.imshow('gray',gray_image)
cv2.waitKey()

#defines list where arrays will be appended into
output_list = []   

#this block of code loops from 0-400, at each integer it loads the corospoonding .npy file from collected data
#each instance of data loaded are the sonar returns 800 long with intensity values ranging from 0-255
#each array at each gradian is appended to the output_list to make one long data set list which can be used to construct an image
for x in range(400):
    gradian = np.load("/home/wrc/Desktop/Github/MICRO_UUV_PERCEPTION/data/"+str(x)+".npy")                                                                    
    output_list.append(gradian)
    
#stacks each numpy array element across columns (along the x axis)
out_arr = np.stack((output_list),axis=0)   


#this block of coud indexes from 0->400 integers, inputting each 400 element array from the outputted list previously
for i in range(400):
    gray_image[i] = output_list[i]
    cv2. imshow('new',gray_image)
    cv2.waitKey(1)                  #allows the full image to construct before closure
