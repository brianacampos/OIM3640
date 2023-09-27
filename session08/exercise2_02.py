#Calculate the sum of the integers from 1 to 10
#create a function
def problem_1():
    """this function will calculate the sum of the integers
    from 1 to 10
    """
    #start at 0 
    number = 0 
    i = 1
    while i < 11:
        number += i
        i += 1
    return number 

print(problem_1())





#Calculate the sum of the integers from 1 to 1000
#create a function
def problem_2():
    """this function will calculate the sum of the integers
    from 1 to 1000
    """
    #start at 0 
    number = 0 
    i = 1
    while i < 1001:
        number += i
        i += 1
    return number 

print(problem_2())



import math

#Calculate the sum of all the odd numbers from 1 to 1000. How about all the even numbers?
#Create a function 
def problem_3(odd=True):
    """this function is going to pull all the odd numbers and sum them up
    it will also be able to do it with positive numbers"""
    #start at 0
    number = 0
    i = 1
    while i < 1001:
        if odd:
            if i % 2 == 1:
                number += i
        else:
            if i % 2 == 0:
                number += i
        i += 1
    return number

print(problem_3(odd=True))
print(problem_3(odd=False))
