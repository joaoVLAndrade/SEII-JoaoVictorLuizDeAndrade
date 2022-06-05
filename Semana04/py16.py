li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li,reverse=True)#Retorna uma nova lista
#li.sort()#Aplica o método na lista original e altera o objeto de referência

#print('Lista original:', li)
#print('Lista ordenada:',s_li)

tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)#Retorna a tupla ordenada em uma lista
#print('Tupla ordenada:', s_tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
#print('Dicionário ordenado:', s_di)#Retorna as keys ordenadas

li = [-2,-1,4,6,7,-10]
s_li = sorted(li, key=abs)
#print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'{self.name}, {self.age}, {self.salary}'
    
e1 = Employee('Carl', '37', 70000)    
e2 = Employee('Sarah', '29', 80000)    
e3 = Employee('John', '43', 90000)    

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

#s_employees = sorted(employees, key=e_sort)
#s_employees = sorted(employees, key=lambda emp: emp.age)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('salary'),reverse=True)

print(s_employees)
        
        