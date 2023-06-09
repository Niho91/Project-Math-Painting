import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.colour

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
