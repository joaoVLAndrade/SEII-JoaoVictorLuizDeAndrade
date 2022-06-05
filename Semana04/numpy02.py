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

#Array operations

#print(2*a0)#Uma lista mutiplicada equivale a repetir essa lista n vezes
#print(2*a1)#A bibiloteca numpy permite realizar operações vetoriais

#print(a1>4)
#print(a1[a1>4])#Printa somente os valores que satisfazem a condição

a1 = a1 + 2
print(a1)

x = np.linspace(0,10,100)
y = x**2
plt.plot(x,y)
plt.show()

plt.hist(a4)
plt.show()


f = lambda x: (x**2)*np.sin(x)

x = np.linspace(0,25,200)
y = f(x)

plt.plot(x,y)
plt.show()