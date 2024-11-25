#Written by Arghya Vyas
notallowed = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'Y']

word = input('').upper()  
if any(letter in notallowed for letter in word):  
    print('NO')
else:
    print('YES')
