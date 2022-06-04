import csv 

html_output = ''
names = []

'''#Primeiro método - Listas
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    # Ignora o cabeçalho e a primeira mensagem - Dados não importantes
    next(csv_data)
    next(csv_data)
    
    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

html_output += f'<p>Atualmente existem {len(names)} contribuidores públicos. Muito obrigado!'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'
    
html_output += '\n</ul>'

print(html_output)
'''

#Segundo método - Dicionários
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    
    # Ignora a primeira mensagem - Dados não importantes
    next(csv_data)
    
    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>Atualmente existem {len(names)} contribuidores públicos. Muito obrigado!'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'
    
html_output += '\n</ul>'

print(html_output)
