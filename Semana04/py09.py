import os
import datetime

#print('Endereço atual: ',os.getcwd()) #Retorna o endereço do diretório atual

os.chdir('C:\\Users\\João\\Desktop') #Altera o endereço de diretório atual para o destino

#print('Novo endereço: ', os.getcwd())

#print('Arquivos do diretório: ', os.listdir()) #Lista os arquivos em um diretório

#os.mkdir(Python) #Permite criar um diretório
#os.mkdir(Python/Teste) #Retorna erro caso o primeiro diretório ainda não tenha sido criado
#os.makedirs('Python/Teste') #Cria uma hierarquia de diretórios
#os.removedirs('Python/Teste') #Remove uma hierarquia de diretórios
#os.rename('1.txt', 'demo.txt') #Renomeia arquivos e diretórios

#mod_time = os.stat('demo.txt').st_mtime #Permite obter informações de um arquivo

#print(mod_time)
#print(datetime.fromtimestamp(mod_time)) #Printa a data de modificação do arquivo de forma legivel

'''#Permite verificar todos os arquivos em uma arvore de diretórios
for dirpath, dirnames, filenames in os.walk('C:\\Users\\João\\Desktop'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
'''

print(os.environ.get('Home'))

file_path = os.path.join(os.environ.get('Home'), 'teste.txt') # Permite a junção de dois caminhos de forma coerente
print(file_path)

'''
print(os.path.basename('/tmp/test.txt')) #Retorna a base do path
print(os.path.dirname('/tmp/test.txt')) #Retorna o nome do diretório
print(os.path.split('/tmp/test.txt')) #Retorna ambos em uma tupla
print(os.path.exists('/tmp/test.txt')) #Verifica a existência do caminho
print(os.path.isdir('/tmp/test.txt')) #Verifica se o caminho aponta para um arquivo 
print(os.path.isfile('/tmp/test.txt')) #Verifica se o caminho aponta para um arquivo
print(os.path.split('/tmp/test.txt')) #Retorna a raiz do arquivo e a extensão do arquivo
'''

