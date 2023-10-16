def matching_ratio(s:str) -> float:
    """
    Return the ratio of matching words in English words, given a string, s

    A matching word is defined as a word that meets both the following two conditions:
        -It contains double the number of letters as the given string
        -It either starts with the same first letter as the given string or ends with the same last letter.
    
    Some useful scaffold code that you can use:

    f = open('data/words.txt') #Open the file "words.txt" that contains a list of English words, one per line

    for line in f: #Iterate through each line, where each line represents an English word (ending with '\n')
    
    """
    #Open the file of text 
    f = open('data/words/txt')

    #We need the total amount of words for this ratio so we should count the total amount of words in this list
    ftotal = count.f

    #Refer to file and apply matching requirements 
    total = 0
    for line in f:
        if line >= (s*2)
            total += 1
        if line in f.firstletter == s.firstletter, line.firstletter == s.lastletter
            total +=1
            
    matching_ratio(total/ftotal)
