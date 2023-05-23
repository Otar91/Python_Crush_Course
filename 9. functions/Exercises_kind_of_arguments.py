#T-sihrt
def make_shirt(size,message):
    print('Your T-shirt is size ' + size.title() +
    ' and your message is: ' + message.title())

make_shirt(size='medium',message="'Hello! everybody'")

#Modifying the last function
#large T-shirt
def make_shirt(size,message='I love Python'):
    print('Your T-shirt is size ' + size.title() +
    ' and your message is: ' + message.title())

make_shirt('medium')