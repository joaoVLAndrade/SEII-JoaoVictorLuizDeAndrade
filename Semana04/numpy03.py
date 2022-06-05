import numpy as np
import matplotlib.pyplot as plt

#Introduction

a0 = [1,10,3,4]
a1 = np.array([1,10,3,4,24,30,10,2,4])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)#Cria um vetor de 0 a 10 com 100 intervalos
a7 = np.arange(0, 10, 0.2)#Cria um vetor de 0 a 10 com espaçamento de 0,2 entre cada amostra

#Array Indexing/Slicing

print(a1[2])#Retorna o terceiro elemento do vetor
print(a1[1:5])#Retorna do elemento 1 até o 4 elemento do vetor
print(a1[a1>4])

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])


#1° Forma
first_letter_j = (np.vectorize(lambda s: s[0])(names)) == 'J' #Define uma função vetorizada que recebe um vetor numpy como entrada e retorna como saida outro vetor
print(first_letter_j)

#2°Forma
v_func = np.vectorize(lambda s: s[0])#Retorna um objeto numpy vetorizado(vetor de função)
bool_j_vector = (v_func(names) == 'J')
print(bool_j_vector)

print(names[first_letter_j])#X e first_letter_j são vetores boleanos e podem ser utilizados para printar somente os valores que comecem com J

print(a1[a1%2 == 0])#Retorna apenas os números divisiveis por 2
