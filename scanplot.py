import matplotlib.pyplot as plt
import numpy as np

#c = [68, 138, 188, 219, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255] #color values from 1 ping 
c = open('test_1.txt','r')
color_data = c.read()  #color intensity dependant on range 
angle = np.arange(200)
x = color_data.size
print(x)
plt.scatter(angle,color_data)
#plt.scatter()
plt.show()
#print(color_data)
#print(angle)
