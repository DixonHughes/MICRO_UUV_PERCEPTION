import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib.colors import Normalize
from matplotlib.text import TextPath


for x in range(400):
    gradian = np.load("/home/wrc/Desktop/Github/MICRO_UUV_PERCEPTION/data/"+str(x)+".npy")
    #print(gradian)
    x_axis = np.ones(200)*x
    y_axis = np.arange(0,200)
    print(y_axis)
    plt.scatter(x_axis, y_axis, c = gradian )
plt.show()



