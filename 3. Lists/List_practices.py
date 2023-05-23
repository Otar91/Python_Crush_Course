bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0].title())

#the psition in a list start at 0 not at 1
print(bicycles[1]);
print(bicycles[3]);

print(bicycles[-1]); #esta es una notacion especial que tiene Python para identificar el ultimo elemento de una lista

#Using individual values from a list
message='My first bicycle was a ' + bicycles[1].title() + '!';
print(message);