import numpy as np
from PIL import Image


#create 3d numpy array of zeros, then replace black zeros with yellow pxls
data = np.zeros((10, 10, 3), dtype=np.uint8)
data[:] = [255, 255, 255]
print(data)

data [0:7, 2:7] = [255, 0, 0]
data [7:10, 5:9] = [255, 255, 133]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
