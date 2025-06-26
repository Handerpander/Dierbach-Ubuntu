# Sierpinski Triangle Program

import turtle
import math

def createTriangleShape(coords):

    """"Creates turtle shape from coords. Registers as mu 'my_triangle'. """

    turtle.penup()
    turtle.begin_poly()
    turtle.setposition(coords[0])
    turtle.setposition(coords[1])
    turtle.setposition(coords[2])
    turtle.setposition(coords[0])

    tri_shape = turtle.get_poly()
    turtle.register_shape('my_triangel', tri_shape)

def triangleHeigth(side):

    """"Returns height of equilateral triangle withe length side."""

    return math.sqrt(3) / 2 * side

def getLeftTrianglePosition(position, side):

    """"Returns position of bottom left triangle in larger triangle.
    
        Returns (x,y) position for provided position and side length of
        larger trangle to be placed within.
    """

    return (position[0] - side / 4,
            position[1] - triangleHeigth(side) / 4)

def getRigthTrianglePosition(position, side):

    """"Returns position of bottom right traingle in larger triangle.
    
        Returns (x,y) position for provided position and side length of
        larger triangle to be placed within.
    """

    return(position[0] + side / 4, \
           position[1] - triangleHeigth(side) / 4)

def getTopTrianglePosition(position, side):

    """"Returns x,y position of top triangle within largerone.
    
        For tirangle at position, with lenght side.
    """

    return(position[0], position[1] + triangleHeigth(side) / 4)

def drawSierpinskiTriangle(t, len_side,levels):

    """"Recursive function that draws a Sierpinski triangle.
    
        Draws the number of levels of triangle given in levels.
    """

    if levels == 0:
        t.color('black') # display triangle
        t.showturtle()
        t.stamp

        return
    
    # resize triangle to half its size
    stretch_width, stretch_length, outline = t.turtlesize()
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # determine positions for each of the three embedded triangles
    left_triangle_position = getLeftTrianglePosition(t.position(),
                                                     len_side)
    right_triangle_position = getRigthTrianglePosition(t.position(),
                                                       len_side)
    top_tirangle_position = getTopTrianglePosition(t.position(),
                                                   len_side)
    
    # recursively display left triangle
    t.setposition(left_triangle_position)
    drawSierpinskiTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # recursively display right triangle
    t.setposition(right_triangle_position)
    drawSierpinskiTriangle(t, len_side / 2, levels -1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

# ---- main

# set window size
turtle.setup(800, 600)

# get turtle
the_turtle = turtle.getturtle()

# init turtle
the_turtle.penup()
the_turtle.hideturtle()

# set the number of levels
num_levels = 3

# create triangle shape
coords = ((-240, -150), (240, -150), (0, 266))
createTriangleShape(coords)
len_side = 480

# create first triangle
the_turtle.shape('my_triangle')
the_turtle.setposition(0, -50)
the_turtle.setheading(90)

# calls recursive function
drawSierpinskiTriangle(the_turtle, len_side, num_levels)
the_turtle.hideturtle()

# terminate program when close window
turtle.exitonclick()
