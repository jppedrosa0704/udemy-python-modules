# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import json
import locale
from datetime import datetime
import string
from pathlib import Path
import os
os.system('cls')

locale.setlocale(locale.LC_ALL, '')
CAMINHO_TXT = Path(__file__).parent / 'aula_183.txt'

def converte_para_brl(numero: float ) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 5, 6)

dados = dict(
    nome = 'João',
    valor = converte_para_brl(1_234_567),
    data = data.strftime('%d/%m/%Y'),
    empresa = 'O.M.',
    telefone = '+55 (81) 987096232'
)

class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_TXT, 'r', encoding='utf-8') as f:
    texto = f.read()

    template =  MyTemplate(texto)
    print(template.substitute(dados))

# with open(CAMINHO_TXT, 'r', encoding='utf-8') as f:
#     texto = f.read()

#     template = string.Template(texto)
#     print(template.substitute(dados))


#------------------------------------------------------------------------------------------------
#                                       OUTRO EXEMPLO
#------------------------------------------------------------------------------------------------

# texto = '''
# Prezado(a) ${nome},

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia ${data}.
# Caso deseje cancelar o serviço, entre em contato com a ${empresa} pelo telefone $telefone.

# Atenciosamente,
# ${empresa},
# '''

# template = string.Template(texto)
# print(template.substitute(dados))
# print(template.safe_substitute(dados)) caso não tenha chave, garante que o texto será enviado.




# print(dados)
# print(json.dumps(dados, ensure_ascii=False, indent=2))