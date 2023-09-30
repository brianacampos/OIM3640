#quiz question 1 

#Create a function 
def convert(usd, target):
    """
    this function will convert the given amount of USD to another currency 
    """
    #do the math with the input
    if target == 'EUR':
        return use * 0.94
    if target == 'CNY':
        return usd * 7.29
    if target == 'JPY':
        return usd * 147.71

print(convert(100, 'CNY'))






#Quiz question 2

def triangle(n):
    for i in range(n):
        print ('*' * (i + 1))

triangle(7)


#challenge 

def triangle_2(n):
    for i in range(1, n+1):
        print(' '* (n-i) + '*' * i)

triangle_2(5) 