import turtle
import math

leo = turtle.Turtle()
print(leo)  # Tells us that leo is refering to the object being defined#

# leo.fd(100) #forward #exercise 1#
# leo.lt(90) #leftturn

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# for i in range (4):
#     leo.fd(100)
#     leo.lt(90)


def square(t):  # exercise 2#
    """ this function takes a parameter named t to draw a square
    """
    for i in range(4):
        t.fd(100)
        t.lt(90)


square(leo)


# Exercise 2.2
def square(t, length):
    """ this function takes a parameter named t, which is a turtlr, and another parameter length, which is a float.
    It should use the turtle to draw a square with side length, length
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(leo, 200)

#Exercise 2.3
def polygon(t, length, n):
    """draws an n-sided regular polygon"""
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

polygon(leo, 100, 8)

#Exercise 2.4
def circle(t, r):
    """draw an approximate circle"""
    circumference = 2 * math.pi * r
    length = circumference / 50
    polygon(t, length, 50)

circle(leo, 200)


#Exercise 2.5
def arc(t, r, angle):
    """ draw an arc with an angle"""
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# arc(leo, 200, 90)
# arc(leo, 200, 360)

#the process of refactoring
def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them. t is a turtle
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polyline(leo, n=4, length=100, angle=90)



turtle.mainloop()
# This prompts the user with anoter tab in which they can only exit out of#
