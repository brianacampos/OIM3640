a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

#Now something to make sure that a value is put out even if it's just 0
d = b**2-4*a*c

if d < 0 :
    print("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("This equation has one solution: "), x
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/2*a
    x2 = (-b+math.sqrt((b**2)-(4*(a*c))))/2*a
    print("This equation has two solutions", x1, "or", x2)
