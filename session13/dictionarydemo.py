def histogram(s):
    """return a dict, key is letter, vlaue is frequency"""
    d = {}
    for letter in s:
        # if letter not in d:
        #     d[letter] = 1
        # else:
        #     d[letter] += 1
        d[letter] = d.get(letter, 0) + 1 #counts each letter and adds it to the sum, when the letter does not exist in the dictionary, it will start at 0 because thats what we said#
        print (d)
    return d


print(histogram('briana'))