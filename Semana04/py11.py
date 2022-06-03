import os 

os.chdir('Diretório de destino')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)#Separa o nome do arquivo da extensão e retorna uma tupla
    
    f_title, f_course, f_num = f_name.split('-')#Retorna uma lista de palavras separadas em '-'
    
    f_title = f_title.strip();#A função strip remove espaços no inicio e no fim de uma string
    f_course = f_course.strip();
    f_num = f_num.strip()[1:].zfill(2)#A função zfill adiciona zeros no inicio de uma string até ela atingir o tamanho indicado
    
    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(f, new_name)