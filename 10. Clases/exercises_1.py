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

#Instance from class

muralla_china = Restaurant('muralla china','comida china')
muralla_china.describe_restaurant()
muralla_china.open_restaurant()
