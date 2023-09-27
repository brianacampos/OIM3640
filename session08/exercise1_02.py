#Calculate the sum of the integers from 1 to 1000
#We will be using a similar method to that of using a for loop to draw a square

#create function that sums the integers
def sum_of_integers():
    """This function will get the first number and add the integers up to 1000"""
    number = 0
    #In order to find the sum, give the range
    #We have to end with 1001 in order to the number 1000 to count, we also started with 1 since the number is already equal to 0
    for i in range(1,1001):
        number += i
    return number 

print(sum_of_integers())