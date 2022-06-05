'''
LEGB
Local, Encosing, Global, Built-in
'''

x = 'global x'

def test():
    #global x
    x = 'local x'
    y = 'local y'
    print(y)
    print(x)
    
test()
print(x)

def test2(z):
    #global x
    x = 'local x'
    y = 'local y'
    print(z)
    
test2('local z')    

m = min([5, 1, 4.1, 3, 4])
print(m)

'''
def min():
    pass

#Um erro será sinalizado pois o python analizará a função definida globalmente antes da função built-in
m = min([5, 1, 4.1, 3, 4])
    print(m)
'''

#Enclosing

def outer():
    x = 'outer x'#Se x for comentado, será printado o inner x e o global x
    
    def inner():
        #nonlocal x #Se o atributo nonlocal for utilizado, podemos alterar o outer x
        x = 'inner x'#Se comentarmos essa linha, será printado o outter x 2 vezes, pois ele envolve a função interna
        print(x)
        
    inner()
    print(x)
    
outer()        
print(x)