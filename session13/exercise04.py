#create a function to create a dictionary of words 
def create_dictionary(f):
    #open the file of words
    f = open('data/words.txt')
    l = {}
    for line in f:
        word = line.strip()
        l[word] = 1
    return l
    
