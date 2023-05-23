#input_exerceises

#7.1 Rental car
prompt='Whata kind of rental card would you like?\n'
prompt+='Please tell us you favourite mark\n'
data=input(prompt)
print('Yuo would a like a ' + data  +
    ' car, let us a moment we going to check')

#Restaurant seating
prompt=input('How many people there are in your dinner group?\n')
group_dinner = int(prompt)
if group_dinner>8:
    print('We need a moment to prepare your table')
else:
    print('Your table is ready')


