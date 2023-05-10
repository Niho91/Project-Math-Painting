from canvas import Canvas
from shape import  Rectangle, Square

canvas_height = int(input("Enter the height of canvas: "))
canvas_width = int(input("Enter the width of canvas: "))
colours = {"white": (255, 255,255), "black": (0, 0, 0)}
canvas_colour = input("Enter canvas colour (black or white): ")
canvas = Canvas(height = canvas_height, width=canvas_width, colour=colours[canvas_colour])

while True:
    shape_type = input("Enter your shape or quit to quit: ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        red = int(input("Enter how much red: " ))
        green = int(input("Enter how much green: "))
        blue = int(input("Enter how much blue: "))
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, colour=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter side of the square: "))
        red = int(input("Enter how much red: "))
        green = int(input("Enter how much green: "))
        blue = int(input("Enter how much blue: "))

        s1 = Square(x=sq_x, y=sq_y, side=sq_side, colour=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")
