#Calculate the sum of the integers from 1 to 10
#We will be using a similar method to that of using a for loop to draw a square

#create function that sums the integers
def sum_of_integers():
    """This function will get the first number and add the integers up to 10"""
    number = 0
    #In order to find the sum, give the range
    #We have to end with 11 in order to the number 10 to count, we also started with 1 since the number is already equal to 0
    for i in range(1,11):
        number += i
    return number 

print(sum_of_integers())

# 2) Using while rewrite all the loops in Exercise 01