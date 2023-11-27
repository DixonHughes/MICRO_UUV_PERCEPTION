import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib.colors import Normalize
from matplotlib.text import TextPath

color = []                                 #this for loop creates a list from the txt file
for line in open("test_1.txt"):
    nums = line.split()
    nums = map(int, nums)

    color.extend(nums)

#Ecolor = int(color())
print(type(color[0]))
angle = np.arange(200)                  #this is the angle in gradians per sonar ping, 400 gradians andd only 1216 returns
y = range(0,200,1)

fig, ax = plt.subplots()
cmap = plt.colormaps["viridis"]
plt.scatter(angle , y, c = color)
fig.suptitle("Sonar Intensity Returns", size = 13) 
ax.set_xlabel("Sonar Angle (gradians)")
ax.set_ylabel("Sonar Range (element-wise)")
plt.colorbar()
plt.show()
