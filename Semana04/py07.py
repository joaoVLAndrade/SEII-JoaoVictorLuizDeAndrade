
def hello_func(name):
    print(f'Hello {name}!')
    
def sum_func(a,b):
    return print(a+b)

hello_func('João')

a = 10
b = 30

sum_func(a,b)
    
'''*Args e **Kwargs permitem passar como parâmetros um número arbitrário de parâmetros.
    *var representa uma lista e **var um dicionário'''
    
#Exemplo: https://medium.com/rafaeltardivo/python-entendendo-o-uso-de-args-e-kwargs-em-fun%C3%A7%C3%B5es-e-m%C3%A9todos-c8c2810e9dc8    
#Autor: Rafael Tardivo

def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
world_cup_titles('Espanha', '2010')

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)

#No primeiro exemplo, o primeiro argumento passado é um nome de pais e em sequência varios argumentos são passados. 
#Se não houvesse o asterisco, um erro seria sinalizado e os titulos não seriam adicionados a lista *args

#No segundo exemplo, utiliza-se **kwargs pois é necessário verificar o id de um atributo. Se esse atributo estiver presente no dicionário, 
#um condicional realiza uma operação.