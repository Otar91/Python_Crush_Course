#Exercise 5.3
from re import L


alien_color='red';
if alien_color=='green':
    print('The player earned 5 points');

alien_color='green';
if alien_color=='green':
    print('The player earned 5 points');

#Exercise 5.4
alien_color='red';
if alien_color=='green':
    print('The player earned 5 points');
else:
    print('Player earned 10 points');

#Exercise 5.5
alien_color='green';
if alien_color=='green':
    print('The player earned 5 points');
elif alien_color=='yellow':
    print('Player earned 10 points');
else:
    print('Player earned 15 points');

#Exercise 5.6
age=45;
if age<2:
    state='baby'
elif age<4:
    state='taddler'
elif age<13:
    state='kid'
elif age<20:
    state='teenager'
elif age<65:
    state='adult'
else:
    state='elder'
print('The person a is '+state.upper())\


