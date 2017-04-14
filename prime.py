number = input('Please enter a number: ')

for i in range(2, int(number)):
    if int(number) % i == 0:
        print('Not prime')
        break
else:
    print('Prime')
