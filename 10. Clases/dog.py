#Define a class call 'Dog', all time we'd to use capitaleze letter to begin a class
class Dog():
    '''A simple attempt to model a dog'''

    #tHE CONSTRUCTOR
    def __init__(self,name,age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age

    #METHODS
    def sit(self):
        '''Simulate a dog sitting in response toa command'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(self.name.title() + ' reolled over!')

#====================================================================================
#MAKING a intance from a class
my_dog=Dog('noah',2) #This is a singual intance created from a class Dog



#====================================================================================
#Accesing attributes
#Para acceder a un atributo usamos la notacion punto=
#nombre de la instancia.nombre del atributo
print("my dog's name is " + my_dog.name.title() +'.')
print("My dog is " + str(my_dog.age) + ' years old.')

#===================================================================================
#Calling methods

#eb los metodos Python revisa por medio de la notacion  punto
#el metodo creado en la clase e importa ese bloque de codigo

my_dog.roll_over()
my_dog.sit()

