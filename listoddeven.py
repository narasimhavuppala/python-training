my_list = [1, 4, 7, 16, 25, 36, 49, 8, 100]

#List comphrension
even_number = [element for element in my_list if element % 2 != 0]

print(even_number)

#Print both even and odd number lists
even_number = []
odd_number = []

for i in my_list:
    if i % 2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)

print('Even number list', even_number)
print('Odd number list', odd_number)
