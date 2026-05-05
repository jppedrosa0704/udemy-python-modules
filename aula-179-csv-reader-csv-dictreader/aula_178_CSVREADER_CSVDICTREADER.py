# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV =  Path(__file__).parent /'aula_178.csv'  #caminho do arquivo aula_178.csv
print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r', encoding='latin-1') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';') #ler em dicionário
    
    for linha in leitor:
        print(linha)

with open(CAMINHO_CSV, 'r', encoding='latin-1') as f:
    leitor = csv.reader(f, delimiter=';')
    print(next(leitor))
    print(next(leitor))
