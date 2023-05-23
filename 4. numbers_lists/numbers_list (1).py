numbers=list(range(1,10));
print(numbers);
numbers.append(0);
print(numbers);
print(min(numbers));#find the minimun numbers into the list
print(max(numbers));#find the maxamun numbers into the list
print(sum(numbers));#sum all elements in the list

#list comprehension
squares=[value**2 for value in range(1,11)];
print(squares);

#Use a for loop to print the numbers from 1 to 20,inclusive.
digits=[];
for digit in range(1,21):
    print(digit);

#Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by
#pressing ctrl-C or by closing the output window.
millions=[];
for million in range(1,1000001):
    millions.append(million)
print(min(millions));
print(max(millions));
print(sum(millions));

#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers=[];
for odd_number in range(1,21,2):
    print(odd_number);

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
trhee_mult=[value*3 for value in range(1,11)]
print(trhee_mult);


#A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube

cubes=[]
for cube in range(1,11):
    print(cube**3);

#Use a list comprehension to generate a list of the first 10 cubes.
cubes=[value**3 for value in range(1,10)]
print(cubes);