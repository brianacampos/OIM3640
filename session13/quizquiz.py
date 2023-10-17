s = [1, 2, 3, 4, 4, 5, 6]

for num in s:
    if num % 2 == 0: 
        s.remove(num)

print(s)

for i range(len(s)):
    if s[i] % 2 == 0:
        s.remove(s[i])