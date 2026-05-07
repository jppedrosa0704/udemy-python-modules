📘 README — Variáveis de Ambiente em Python (os.getenv, os.environ, .env)
Este projeto demonstra como trabalhar com variáveis de ambiente em Python utilizando:

os.getenv()

os.environ

Arquivo .env

Biblioteca python-dotenv

O objetivo é mostrar como proteger informações sensíveis (senhas, usuários, hosts, tokens, etc.) sem deixá-las expostas no código.

🔧 Tecnologias utilizadas
Python 3.x

Biblioteca python-dotenv

Módulo padrão os

📦 Instalação das dependências
Antes de executar o script, instale o pacote:

bash
pip install python-dotenv
📁 Estrutura recomendada
Código
seu_projeto/
│
├── .env
├── .env-example
├── script.py
└── README.md
🔐 Criando o arquivo .env
Crie um arquivo chamado .env na raiz do projeto:

Código
BD_HOST=localhost
BD_USER=admin
BD_PASSWORD=senha_super_secreta
BD_PORT=5432
⚠️ Nunca envie o .env para o GitHub.  
Use um .env-example para mostrar o formato:

Código
BD_HOST=
BD_USER=
BD_PASSWORD=
BD_PORT=
🧠 Como o código funciona
O script:

Carrega o arquivo .env com load_dotenv()

Lê variáveis de ambiente usando os.getenv()

Pode definir variáveis dinamicamente com os.environ['VAR'] = valor

🧪 Exemplo de código
python
import os
from dotenv import load_dotenv

# Carrega o arquivo .env
load_dotenv()

# Lendo variáveis de ambiente
print(os.getenv('BD_PASSWORD'))
print(os.getenv('BD_HOST'))
print(os.getenv('BD_USER'))
print(os.getenv('BD_PORT'))

# Exemplo de criação dinâmica (não persiste no sistema)
# os.environ['BD_PASSWORD'] = 'valor temporário'
💻 Como definir variáveis de ambiente no terminal
🔹 Windows CMD
cmd
set SENHA=meu_valor
echo %SENHA%
🔹 Windows PowerShell
powershell
$env:SENHA="meu_valor"
echo $env:SENHA
🔹 Linux / macOS
bash
export SENHA="meu_valor"
echo $SENHA
🛡️ Por que usar variáveis de ambiente?
Evita expor senhas no código

Permite trocar credenciais sem alterar o script

É prática recomendada em aplicações profissionais

Facilita deploy em servidores e containers
