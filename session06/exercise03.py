#question 3.1
#draw 60 squares, turning right 5 degrees after each square

import turtle
import math

leo = turtle.Turtle()
print(leo)  # Tells us that leo is refering to the object being defined#

#loop for number of squares 
def square(t):
    for i in range(60):
        #loop for drawing each square
        for j in range(4):
            t.fd(100)
            t.rt(90)

        #turning 5 degrees
        rt(5)

square(leo)


turtle.mainloop()