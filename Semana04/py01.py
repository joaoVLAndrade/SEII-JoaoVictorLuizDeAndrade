import os

clear = lambda: os.system('cls')

from sys import get_coroutine_origin_tracking_depth


message = 'Hello World'#

print(message)

#Manipulação de strings

print(message[0])#Printa o primeiro caracter da string
print(message[5:])#Printa a partir do quinto caracter da string
print(message[0:3])#Printa a partir do index 0 até o terceiro index sem inclui-lo

print(len(message))#Printa o tamanho da string

#Métodos

print(message.lower())#Utiliza o método lower de strings 
print(message.upper())#Utiliza o método upper de strings 
print(message.count('l'))#Permite a contagem de incidências de uma expressão

new_message = message.replace('World','Universe')#Realiza a substituição de uma expressão por outra
print(new_message)

greeting = 'Hello'
name = 'João'

print(greeting + ' ' + name + '. Welcome!')#Concatenação de strings

message = '{}, {}. Welcome!'.format(greeting,name)#Aplicação do método format para substituição de variaveis através dos placeholders
print(message)

message = f'{greeting}, {name}. Welcome!'#Alternativa para o método format
print(message)

print(help(str))#Retorna as informações sobre um objeto