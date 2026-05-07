# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os
from dotenv import load_dotenv  # type: ignore

load_dotenv() #carrega o arquivo dotenv para ter acesso as variáveis

#os.environ['BD_PASSWORD'] = 'JP É O MAIOR'  #configura as variaves de ambiente

print(os.getenv('BD_PASSWORD'))
print(os.getenv('BD_HOST'))
print(os.getenv('BD_USER'))
print(os.getenv('BD_PORT'))
# print(os.environ) #mostra todaas as variaves de ambiente do meu sistema



#set SENHA=VALOR_QUE_EU_QUERO (No terminal cria uma variável de ambiente)
# SENHA = os.getenv('SENHA') # Imprime a variável de ambiente.
# print(SENHA)
