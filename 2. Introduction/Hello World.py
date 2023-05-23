z='Hello World'
print(z)
#Segunda practica
name='JEIFER martinez';
print(name.title())#muestra el string de la siguiente forma la primera letra de cada palabra en mayuscula y el resto en minusculas
print(name.upper())#El estring se muestra todo en mayusculas
print(name.lower())#El estring se muestra todo en minusculas

#Combaning or concatering strings
first_name='ada';
last_name='corzo';
full_name=first_name+" "+last_name;
print(full_name.title());
print("Hello"+" "+full_name.upper()+'!');
massege="Hello"+" "+full_name.upper()+'!';
print(massege.title())

#Adding whitespace to string with tabulate or Newlines
print("\tPython");
print("Python");
print("Some programming Lenguages:\nPython\n\tMatlab");

#Eliminate whitespaces method
lenguages = "   Python   "
print(lenguages)
print(lenguages.strip())

