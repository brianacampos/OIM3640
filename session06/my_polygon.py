import turtle

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


turtle.mainloop()
# This prompts the user with anoter tab in which they can only exit out of#
