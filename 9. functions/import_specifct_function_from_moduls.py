# from module_name inport function_name
from pizza import make_pizza
make_pizza(16,'pepperoni')

#se pueden importar tantas funciones de uin modulo como se desee
#from modelu_name import function_0, function_1.... Se separan por coma

#making an alias to a function
from pizza import make_pizza as mp
mp(16,'pepperoni')

#making an alias to a entering module
import pizza as p
p.make_pizza(12,'pepperoni','mushrooms')

#Import all ther function in a module
from pizza import *
#The * tell's pithon to import all the functions in the module