import matplotlib.pyplot as plt
import numpy as np
import sys 
np.set_printoptions(threshold=sys.maxsize)

import matplotlib as mpl
from matplotlib.colors import Normalize
from matplotlib.text import TextPath
from PIL import Image as im

output_list = []    #defines list where arrays will be appended into
for x in range(400):
    gradian = np.load("/home/wrc/Desktop/Github/MICRO_UUV_PERCEPTION/data/"+str(x)+".npy")
    #print(type(gradian))
    output_list.append(gradian)
    x_axis = np.ones(400)*x
    y_axis = np.arange(0,400)
    plt.scatter(x_axis, y_axis, c = gradian )
#plt.show()
#print(output_list)
out_arr = np.stack((output_list),axis=1)    #stacks each numpy array element across columns (along the x axis)
print(out_arr)

pic = im.fromarray(out_arr)         #converts to image 
pic.save('dummypic.png')
