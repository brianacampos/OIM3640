#Calculate the sum of all the odd numbers from 1 to 1000. (hint: check out range() function in Python documentation.) How about all the even numbers?

#Create a function 
def sum_of(odd=True):
    """this function is going to pull all the odd numbers and sum them up
    it will also be able to do it with positive numbers"""
    number = 0 
    for i in range(1,1001):
        if odd:
            if i % 2 == 1:
                number += i
        else:
            if i % 2 == 0:
                number += i 
    return number 

#this will print the sum of the odd numbers
print(sum_of(odd=True))

#this will print the sum of the even numbers 
print(sum_of(odd=False))