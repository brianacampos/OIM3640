"""
Question 1:

Write a function that prompts the user for an amount in USD (float), converts it to the equivalent amount in Euro (EUR), and prints the result.

Currency Conversion Rates:

1 USD = 0.94 EUR

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. the code that calls the function.
"""
#1 ask user for an input 
num = float(input("Enter the currency in USD: "))

#2 create function that does the math
def convert(num)
"""this function will convert the USD amount to EUR"""
   change = num / 0.94
   return change


#3 call the function 
#4 print the result 
print(convert(num))