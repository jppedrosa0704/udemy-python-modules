Envio de E-mail com Python 📧🐍

Projeto simples para envio de e-mails utilizando Python, SMTP do Gmail e templates HTML.

O projeto demonstra:

envio de e-mail com smtplib
utilização de HTML no corpo do e-mail
variáveis de ambiente com .env
uso de Template para personalização
autenticação SMTP com Gmail
📚 Tecnologias utilizadas
Python 3
smtplib
email.mime
python-dotenv
📂 Estrutura do projeto
projeto/
│
├── main.py
├── aula_185.html
├── .env
├── .env-example
├── .gitignore
└── requirements.txt
⚙️ Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Entre na pasta:

cd seu-repositorio

Instale as dependências:

pip install -r requirements.txt

Ou instale manualmente:

pip install python-dotenv
🔐 Configurando o .env

Crie um arquivo .env:

FROM_EMAIL=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
⚠️ Gmail e senha de app

O Gmail não permite login usando sua senha normal da conta em aplicações SMTP.

Você precisa criar uma Senha de App na sua conta Google.

Documentação oficial:

Conta Google - Senhas de app
📄 .env-example
FROM_EMAIL=
EMAIL_PASSWORD=
📨 Template HTML

Arquivo aula_185.html:

<h1>Olá, ${nome}!</h1>

<p>Este é um e-mail enviado com Python.</p>
🐍 Código principal
import os
from pathlib import Path
from dotenv import load_dotenv
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

CAMINHO_HTML = Path(__file__).parent / 'aula_185.html'

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

with open(CAMINHO_HTML, 'r', encoding='utf-8') as f:
    texto_arquivo = f.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo("localhost")
    server.starttls()
    server.ehlo("localhost")
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)

    print('E-mail enviado com sucesso!')
🚀 Executando o projeto
python main.py
✅ Funcionalidades
Envio de e-mail HTML
Template dinâmico
Variáveis de ambiente
SMTP com Gmail
Estrutura simples e reutilizável
🔒 Boas práticas

✅ Nunca envie o .env para o GitHub
✅ Adicione .env no .gitignore
✅ Utilize senha de app do Google
✅ Nunca exponha credenciais no código

📌 Exemplo de .gitignore
