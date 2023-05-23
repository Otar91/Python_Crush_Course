#Exercise 8.9
magicians = ['Houdini','coperphill','Merlin']

def show_magicians(magicians):
    for magician in magicians:
        print('The next magician is ' + magician.title())

show_magicians(magicians)

#Exercise 8.10
def unchanged_magicians(magicians):
    magicians1=magicians[:] #copio la lista original y trabajo con ella para evitar modificarla
    for magician1 in magicians1:
        print('The next great magician is ' + magician1 + '!')

unchanged_magicians(magicians)