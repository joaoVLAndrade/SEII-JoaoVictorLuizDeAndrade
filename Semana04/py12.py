import csv

#1° Método - Listas
'''
with open('names.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file)#retorna um objeto que pode ser iterado, onde cada iteração representa uma linha de um arquivo csv em formato de lista separados por um delimitador que pode ser especificado.#É importante especificar o delimitador ou a separação não sera feita corretamente.
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t', lineterminator='\n')#retorna um objeto responsável por escrever os inputs do usuário, no arquivo indicado como argumento
               
        for line in csv_reader:#Para cada linha no arquivo de leitura, será escrito uma nova linha no novo arquivo
            csv_writer.writerow(line)
'''

#2° Método - Dicionários

with open('names.csv', 'r') as csv_file: 
    csv_reader = csv.DictReader(csv_file)#retorna um objeto que pode ser iterado, onde cada linha do arquivo é dada por um dicionário onde as keys são dadas pelos valores do cabeçalho e os values os valores dos campos
    
    '''
    for line in csv_reader:
        print(line)
    '''
    
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email', 'teste']#É necessário especificar os campos que poderão ser escritos no arquivo. Caso o dicionário de input tenha keys não indicadas, é necessário remove-las do processo de escrita
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t', lineterminator='\n')#retorna um objeto capaz de escrever os inputs do usuário
        
        csv_writer.writeheader()#Escreve o cabeçalho(fieldnames)
    
        for line in csv_reader:
            #del line['email']
            csv_writer.writerow(line)