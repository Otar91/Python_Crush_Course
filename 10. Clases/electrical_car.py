#Inheritance

#Parent Class

#Notes: when you create a child class, the parent class must be part of the current file
#       and must appear before the child class in the file.


class Car():
    '''A simple attempt to represent a car'''

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        long_name= str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

#Child class
#The name of the parent class must be included in parenthesis in the 
#definicion of the child class
class Electrical_car(Car):
    '''Represent aspects of a car, specific electric vehicles'''

#The init method() takes in the information required to make a car class
    def __init__(self,make,model,year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make,model,year)
        self.battery_size=70
#The super() method helps Python to make connections bewteeen a parent class
#and a child class

#Specific methods() to a child class
    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')

#Instances as attributes
class Battery():
    ''' A simple attempt to model a battery for an electric car'''

    def __init__(self,battery_size=70):
        '''Initialize the battery attributes.'''
        self.battery_size=battery_size  
    
    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')


#Override Methods from the parent class

# To do this you define a method in the child class with the same name 
# as the method you want to override in the parent class.
    def fill_gas_tank():
        '''Electric cars don't have a gas tank'''
        print("This car doesn't have a gas tank!")



#Instance a object
my_tesla = Electrical_car('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()





