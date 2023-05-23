#The modulo operator
age=4%3
print(age)

#even or odd
data = input('Enter a number and I tell you whether is even or odd:\n')
number=int(data)
number_1 = number % 2
if number_1 == 0:
    print('The number '+ data +' is even')
else:
    print('The number ' + data + ' is odd')
