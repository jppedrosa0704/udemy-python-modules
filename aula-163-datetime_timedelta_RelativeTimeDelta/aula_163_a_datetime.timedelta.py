
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('29/04/2026 20:00:23', fmt)
data_fim = datetime.strptime('22/08/2030 22:35:25', fmt)
# print(data_inicio > data_fim)
# print(data_inicio < data_fim)
# print(data_inicio == data_fim)

#timedelta
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())


#somando dias horas e segundos

delta = timedelta(days=10, hours=2, seconds=30)
print(data_fim + delta)
