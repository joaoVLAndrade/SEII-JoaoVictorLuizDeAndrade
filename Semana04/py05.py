import os
from time import sleep

clear = lambda: os.system('cls')
clear()


a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = 9

if a > b:
    print(f"{a} é maior que {b}")
elif a < b:
    print(f"{a} é maior que {b}")
else:
    print(f"{a} é igual a {b}")

lista_1 = [1,2,3,4]
lista_2 = lista_1


if lista_1 is lista_2:
    print("A lista 2 se refere ao mesmo objeto da lista 1.\n")
else:
    print("As listas são objetos diferentes.")    
    
lista_2 = lista_1.copy()    

if lista_1 is lista_2:
    print(f"A lista 2 revere ao mesmo objeto da lista 1.")
else:
    print("Agora as listas são objetos diferentes.")
    
if 5 not in lista_1 and lista_1.__len__() <= 4:
    lista_1.append(5)
    
print(lista_1)

# O python considera os seguintes valores como falsos:
# False
# None
# Zero de qualquer tipo númerico
# Sequências vazias. Por exemplo: '',(),[]
# Um dicionário vazio.

    