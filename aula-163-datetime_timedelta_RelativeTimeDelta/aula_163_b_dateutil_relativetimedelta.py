from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('29/04/2026 20:00:23', fmt)
data_fim = datetime.strptime('22/08/2030 22:35:25', fmt)
relatorio = relativedelta(data_fim, data_inicio) #data relativa
print(relatorio.days, relatorio.years) #diferenca dos dias e anos
print(relatorio)

#time delta é possivel somar, subtrair e etc.. entre as duas datas desejadas.
delta = timedelta(days=10, hours=2)
print(data_fim - delta)
print(data_fim + relativedelta(seconds=60, minutes=10))



print(data_fim + relativedelta())