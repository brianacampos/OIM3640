#question 3.1
#draw 60 squares, turning right 5 degrees after each square

import turtle
import math

leo = turtle.Turtle()
print(leo)  # Tells us that leo is refering to the object being defined#

#loop for number of squares 
def square(t, length):
    for i in range(4):
        #loop for drawing each square
        t.fd(length)
        t.lt(90)

def multiple(t, n, length, angle):
    for i in range(n):
        square(t, length)
        t.rt(angle)

multiple(leo, 60, 100, 5)


turtle.mainloop()