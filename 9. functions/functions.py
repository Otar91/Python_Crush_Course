#The first function
def greet_user():
    '''Display a simple greeting.'''
    print('Hello.')

greet_user()

#modifcy sligtly our first function
def greet_user(username):
    '''Display a simple greeting.'''
    print('Hello ' + username.title())

greet_user('Albeiro')

#Display messange
def message():
    '''Just display a simple messange'''
    print('In this chapter I am learning about function')

message()

def favorite_book(book):
    print('My favorite book is :' + book.title())

favorite_book('the old war')
