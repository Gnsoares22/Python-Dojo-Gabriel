from datetime import date, datetime, timedelta
import time

data_atual = datetime.today() # pega a data de hoje
print(data_atual.strftime("%d/%m/%y")) #formata data 

horario = time.strftime("%H:%M:%S", time.localtime()) #formata e pega a hora atual 
print(horario)

data_velha = '01/01/2016 00:00:00'
data_convertida = datetime.strptime(data_velha,"%d/%m/%Y %H:%M:%S")
print(data_convertida)

diferenca = data_convertida - timedelta(days= 365) #subtração de datetime (timedelta)
print(diferenca)
