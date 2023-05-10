class Square:

    def __init__(self, x, y, side, colour):
        self.x = x
        self.y = y
        self.side = side
        self.colour = colour

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.colour


class Rectangle:

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.colour


class Rectangle2:

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.colour
