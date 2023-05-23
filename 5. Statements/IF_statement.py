#IF statement

#Checking for Equality 
cars=['audi','bmw','subaru','toyota'];
for car in cars:
    if car == 'bmw':
        print(car.upper());
    else:
        print(car.title());

#Checking for inequality
requested_topping='mushrooms';
if requested_topping!='anchovies':
    print('Hold the anchovies');

#Using 'and' to check multiple conditions
age_0=22;
age_1=18;
if (age_0 >=21) and (age_1>=21):
    print('Both are they are 21');
else:
    print('They are not 21 yeras old');

#using 'or' to check multiple conditions
if (age_0>=21) or (age_1>= 21):
    print("With 'or' the only way to fail is if both test fail.")

#Checking whether a value in a list
requested_toppings=['mushrooms','onios','pinapples'];
if 'mushrooms' in requested_toppings: #Palabra clave 'in'
    print('yes, there are mushrooms');

#Checking wheter a value is not in a list
banned_users=['andrew','carolina','david']; 
user='marie';

if user not in banned_users: #Palabras claves 'not in'
    print('The user '+user+' can comment');



