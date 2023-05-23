magicians=['alice','david','carlos'];
for magician in magicians:
    print(magician.title());

#working with for loop
magicians=['alice','david','carlos'];
#into the for loop all the next lines are indented
for magician in magicians:
    print(magician.title() + ', that was a great trick');
    print('I cant wait to see your next trick, '+magician.title()+'\n');

#Aqui se acaba el for loop because the next line dont has idented
print('Thank you, everyone. That was a great magic show');
