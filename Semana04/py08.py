#import sys
#sys.path.append('diretório do módulo')#Permite que módulos sejam importados de diretórios diferentes

import math
import random
import datetime
import os

#import my_module #Importa toda a biblioteca
#import my_module as mm #Importa a biblioteca e atribui um apelido para ela
#from my_module import find_index,test as verification #Importa uma ou mais partes da biblioteca
from my_module import * #Permite importar partes da biblioteca de acordo com a demanda


courses = ['History','Math','Physics', 'CompSci']

#index = my_module.find_index(courses, 'Math')
#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')

print(index)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(os.getcwd())