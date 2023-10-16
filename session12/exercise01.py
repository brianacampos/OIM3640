# Exercise 01
# What is the index of 'Apple'? 
# the index would be L[0][0] because it is in the first list (always starts at 0)
#     and it is the first in that list so 0

# 'Lisa'? 
# The index would be L[2][2] because it is in the third list (0,1,2)
    # and it is the third in the list (0,1,2)

# 'On Rail'?
# The index would be L[1][2][1] because it is in the second list (1), 
    #the list starts at the third name (2) and the word can be found second (1)

#Index is basically a way to access and retrieve the respective elements within the given list L

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]





# Q. What is the length of the following list?
#It would be = to 4 where:
    # Element 1: 'spam'
    # Element 2: 1
    # Element 3: ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants'] (a list containing four elements).
    # Element 4: [1, 2, 3] (a list containing three elements).


my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))






t = ['a', 'b', 'c', 'd', 'e', 'f']


# Q. How do we get ['b', 'c']? 
sublist1 = t[1:3]
print(sublist1)

# ['a', 'b', 'c', 'd']? 
sublist2 = t[0:4]
print(sublist2)

# ['d', 'e', 'f'] ? 
sublist3 = t[3:6]
print(sublist3)

# The entire list?
sublist4 = t[:]
print(sublist4)