#9,6 Ice-cream stand
class Restaurant():
    '''A class to characterize a restaurant'''

#constructor
    def __init__(self,restaurant_name,cuisine_type):
        '''Inicialitize the class'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

#methods
    def describe_restaurant(self):
        print("The restaurant's name is: " + self.restaurant_name.title())
        print("It's cuisine type is: " + self.cuisine_type.title())

    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name.title() + ' in now open')


class IceCreamStand(Restaurant):
    '''Represent the stand of ice cream in restaurants'''

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
    
    def cream_flavors(self):
        print("here are 3 flavor's ice cream:\n")
        print('-Chocolate')
        print('-vanilla')
        print('-chicle')

tests1 = IceCreamStand('Muralle china','Chinese cuisine')
tests1.cream_flavors()




