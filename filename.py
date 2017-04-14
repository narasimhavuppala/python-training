# Python program to print the file extension in a given file name
#Ex: Hello.java should output java

file_name = input('Please enter a file name: ')

print(str(file_name.split('.')[-1]))
