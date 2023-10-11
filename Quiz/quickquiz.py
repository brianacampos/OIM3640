def any_uppercase1(s):
    for c in s:
        if 'c'.isupper():
            return True
        else:
            return False

def any_uppercase3(s):
    for c in s:
        flag = c.isupper()
    return flag

print(any_uppercase3('iPhone'))
print(any_uppercase3('Babson'))
print(any_uppercase3('NBA'))
