import os
from pathlib import Path
from dotenv import load_dotenv # type ignore
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

#caminho do arquivo html
CAMINHO_HTML = Path(__file__).parent / 'aula_185.html'



#dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

#configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smpt_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#Mensagem de texto

with open(CAMINHO_HTML, 'r', encoding='utf-8') as f:
    texto_arquivo = f.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

#transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


#envia o E-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo("localhost")
    server.starttls()
    server.ehlo("localhost")
    server.login(smpt_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')


