
'''
file = open("Teste.txt",'r')

print(file.name)

file.close()
'''

#Gerenciamento de contexto - Permite a manipulação de arquivos de maneira segura
from ctypes import sizeof


with open('Teste.txt','r') as file:
    #print(file.mode)#Retorna o modo de abertura do arquivo
    '''
    file_contents = file.read() #Esse modo de leitura pode ocasionar erros quando tentarmos ler arquivos grandes pois realiza a leitura do arquivo de uma só vez
    print(file_contents)
    '''
    '''#Dessa forma, serão printadas uma linha de cada vez
    file_content = file.readline()
    print(file_content)
    file_content = file.readline()
    print(file_content)
    file_content = file.readline()
    print(file_content)
    '''
    '''#Este método permite a leitura de arquivos de forma iterativa e sem sobrecarregar o armazenamento de variaveis
    for line in file:
        print(line, end='')
    '''
    #file_contents = file.read(10)#file.read() permite que o usuário escolha a quantidade de caracteres que serão lidos
    #file.seek(0)#Permite ao usuário posicionar o ponteiro de leitura
    '''Este método permite um maior controle do usuário sobre o que será lido
    file_contents = file.read(10)
    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = file.read(10)
    '''
#print(file.closed)    

with open('Teste1.txt','r+') as f:#Se o arquivo ainda não existir, será criado um novo arquivo. Caso contrário, o arquivo existente será sobrescrito
    f.write('Teste 1')
    f_contents = f.readline()
    f.seek(len(f_contents))
    f.write('\nTeste 2')
   
#Método para cópia de arquivos com controle de texto 
with open('Teste.txt','r') as rf:
    with open('Copia_Teste.txt','w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

s = 'c2'
print(len(s.encode('utf-8')))