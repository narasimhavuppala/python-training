# Python program to print number of digits and characters in an input string
# Ex: Python 3.6 should print # of digits = 2 and # of characters = 6

str_input = input('Please enter: ')

d = l = 0

for i in str_input:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        l += 1
    else:
        pass

print('Number of digits=', d)
print('Number of characters=', l)
