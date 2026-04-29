# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_str_data = "2026-04-29 12:04:23"
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data1 = datetime.strptime(data_str_data, data_str_fmt)
print(data1)
data2 = datetime(2026, 4, 29, 12, 1, 00)
print(data2)
# data = datetime(2026, 4, 29, 12, 1, 00, tzinfo=timezone('Asia/Tokyo'))
# print(data)
