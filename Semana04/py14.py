import datetime
from time import strptime
import pytz

#formata um conjunto de inteiros no formato de data
date1 = datetime.date(2016, 7, 24) #O método date permite trabalhar com anos, meses e dias
#print(date1)

#Retorna a data de hoje
today = datetime.date.today()
#print(today)#print(today.year)
#print(today.weekday())#Retorna o número do dia da semana Domingo = 0 ~ Sabado = 6
#print(today.isoweekday())##Retorna o número do dia da semana Domingo = 1 ~ Sabado = 7

tdelta = datetime.timedelta(days=7)#Permite criar uma variação de tempo e realizar operações temporais

#print(today + date1)

bday = datetime.date(2022, 10, 9)

till_bday = bday - today
print(till_bday.days)

#É possível subtrair datas para obter um deltatime ou somar um detaltime para obter-se uma data. Não é possível somar duas datas

#O método time permite trabalhar com horas,minutos, segundos e milissegundos 
t = datetime.time(9,30,45, 10)
#print(t)

#O método datetime permite trabalhar com os valores dos métodos date e time
dt = datetime.datetime.today()
#print(dt)

tdelta = datetime.timedelta(days=5,hours=12)
#print(dt+tdelta)

dt = datetime.datetime(2016, 7, 27,12, 30, 45, tzinfo=pytz.UTC)
#print(dt)


dt_today = datetime.datetime.today()#Retorna a data atual do computador(mesmo fuso) 
dt_now = datetime.datetime.now(tz=pytz.UTC)#Retorna o horário atual em um timezone especificado
dt_utcnow = datetime.datetime.utcnow()#Retorna a hora Coordinated Universal Time, +3h de mg

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt_udi= dt_now.astimezone(pytz.timezone('Etc/GMT-3'))
print(dt_udi)

print(dt_udi.isoformat())
print(dt_udi.strftime('%B %d, %Y'))#Permite printar a data em diferentes formatos

dt_str = 'June 05, 2022'

dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')#Converte uma string para formato de data
print(dt)
