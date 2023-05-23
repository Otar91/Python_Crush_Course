class User():
    
    def __init__(self,first_name,last_name):
        '''Attempt to describe user info into a web page'''
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print('Info user: \n' + 
        self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print("Hello! " + self.first_name.title() + 
        ' ' + self.last_name.title() + ' welcome back!')


class Admin(User):

    def __init__(self,first_name,last_name):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Your privileges as Admin are: ")
        for privile in self.privileges:
            print('-' + privile)



#Create a instance
user_1 = User('joseph','celi')

user_1.describe_user()
user_1.greet_user()
admin1= Admin('jeifer','martinez')
admin1.show_privileges()

