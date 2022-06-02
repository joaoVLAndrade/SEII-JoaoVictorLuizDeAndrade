#Dicionários

from re import S
from turtle import st


student = {'name':'John', 'age':25, 'courses': ['Math','CompSci','Physics']}

print(student)
print(student['name'])
print(student.get('age'))#O método get retorna o valor de uma chave se ele existir. Se não, ele retorna uma mensagem
print(student.get('phone', 'Not Found!'))

#Atualizando o dicionário

student['name'] = 'Jorge'
student.update({'age':17, 'phone': '555-5555'})#O método update permite a atualização de várias chaves ao mesmo tempo, bem como a criação de novas chaves
print(student)

phone = student['phone']
del student['phone']#Removendo uma chave de um dicionário

print(student)
print(student.items())#Printa as chaves e valores de um dicionário

for key,value in student.items():#Iteratividade em dicionários
    print(key,value)