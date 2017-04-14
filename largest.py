#Largest number in a list
# [3, 44, 2, 6]
#sort()

list1 = [3, 44, 2, 6]

max = list1[0]

for i in list1:
    if i > max:
        max = i

print('Largest number is', max)
