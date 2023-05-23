#'If else' statement
age=17;
if age>=18:
    print('You are old enough to vote')
    print('Have you registered to vote jet?')
else:
    print('Sorry you are too young to vote')
    print('Please register to vote as soon you turn eighteen')

#The if-elif-else Chain
#En este tipo de cdena Python analiza cada condicion en sentido descendiente 
# y cuando encuentra una condicion que se cumpla ejecuta ese bloque y omite el resto

age=15;
if age<4:
    print('You ticket is free');
elif age<=18:
    print('You ticket cost $5');
#en else no se necesita poner ninguna condicion porque se ejecutara siempre que las otras dos no se cumplan
else:
    print('You ticket cost $10');


#Using multiple elif blocks
age=12;
if age<=4:
    price=0;
elif age<=18:
    price=5;
elif age <65:
    price=10;
else:
    price=5;
print('Your admision cost is $'+str(price)+'.') 

#Omitting the else block
#The else test sometimes is not necesary
#Si ningun elif no se cumple no se ejecuta ninguna condicion se omite ese bloque
age=14;
if age<=4:
    price=0;
elif age<=18:
    price=5;
elif age <65:
    price=10;
elif age>=65:
    price=5;
print('Your admision cost is $'+str(price)+'.') 



