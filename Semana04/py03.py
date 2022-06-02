#Listas

import os
import time

clear = lambda: os.system('cls')

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_1 = ['Geo', 'Bio']


print(courses)
print(courses[1])#Printa o segundo termo da lista
print(courses[-1])#Printa o ultimo termo da lista
print(len(courses))#Printa a quantidade de itens na lista
print(courses[1:3])#Printa a partir do index 1 até o index 3 sem inclui-lo

print(courses.index('Math'))#Retorna o index da primeira ocorrência de um item em uma lista

courses.append("Art")#Adiciona um elemento no final da lista
print(courses)

courses.pop()#Remove um item de uma lista
courses.insert(2,'Art')#Insere um item no index selecionado
print(courses)
courses.extend(courses_1)#Insere elemento por elemento de uma lista. O método apende enxerga uma lista inteira como um objeto e não cada parte.
print(courses)
courses.append('Math')
courses.remove('Math')#Remove a primeira ocorrência de um item
print(courses)

courses.reverse()#Inverte a ordem de uma lista
print(courses)

time.sleep(2)

clear()
num = [1, 4, 9, 3]
num_2 = num.copy()#Retorna uma cópia da lista

num.sort()
num_2.sort(reverse=True)
print(f'Lista original: {num}\nLista descrescente: {num_2}')

print(max(num))#Retorna o maior valor de uma lista
print(min(num))#Retorna o menor valor de uma lista
print(sum(num))#Retorna a soma de uma lista
    
num.append(1)


for index,num in enumerate(num, start=2):
    print(index, num, end=';\n')


courses_str = ', '.join(courses)#Concatena um número ilimitado de strings.

print(courses_str)

new_list = courses_str.split(', ')#Retorna uma lista de palavras de uma string
print(new_list)


#Tuplas

#As tuplas funcionam de maneira semelhante as listas, porém são imutaveis 

time.sleep(2)

clear()

tuple_1 = tuple(courses)
#tuple_1[0]= '1' #Um erro será indicado caso tentemos alterar uma tupla

#Conjuntos

#Conjuntos são similares a listas , porém não podem ser ordenados e não possuem valores repetidos

lista = [1, 3, 4, 5, 6, 4, 4, 5]
conjunto_1 = set(lista)
conjunto_2 = {1,9,8,3}


print(conjunto_1)

#Exemplos de métodos para conjuntos

print(conjunto_1.intersection(conjunto_2))
print(conjunto_1.union(conjunto_2))


#Para criar um set vazio é necessário utilizar a função set(), caso utilizemos set = {} será criado um dicionário
