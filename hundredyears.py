#Name and age from the user
#Print the exact year when the user will be 100 years old

import datetime

#Get the name from the user
name = input('Please enter your name: ')

#Get the age from the user
age = input('Please enter your age: ')

current_year = datetime.datetime.now().year

hundred_years = current_year - int(age) + 100

print(name + ' you will be hundred years on ' + str(hundred_years))
