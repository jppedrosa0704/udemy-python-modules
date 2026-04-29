from datetime import datetime
from pytz import timezone

dataTokyo = datetime.now(timezone('Asia/Tokyo'))
dataSaoPaulo = datetime.now(timezone('America/Sao_Paulo'))
dataRecife = datetime.now(timezone('America/Recife'))
dataChina = datetime.now(timezone('Asia/Shanghai'))
print(dataTokyo)
print(dataSaoPaulo)
print(dataRecife)
print(dataChina)