a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

# #Now something to make sure that a value is put out even if it's just 0
# d = b**2-4*a*c

# if d < 0 :
#     print("This equation has no real solution")
# elif d == 0:
#     x = (-b+math.sqrt(b**2-4*a*c))/2*a
#     print("This equation has one solution: "), x
# else:
#     x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/2*a
#     x2 = (-b+math.sqrt((b**2)-(4*(a*c))))/2*a
#     print("This equation has two solutions", x1, "or", x2)

#first i will import math so that it makes finding the solution straightforward
import math

#use given function 
def quadratic(a, b, c):
    """
    this function will be able to solve a quadratic equation and return the values of two roots
    """
    #calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    #calculate the roots of the quadratic equation
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    #RETURN the values 
    return root1, root2

#call the function with the given inputs 
print(quadratic(a, b, c))
