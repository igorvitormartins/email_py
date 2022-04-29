from lendo_ini import Lendo_ini
import os
from datetime import datetime
import time
import smtplib
import email.message


def enviar_email(email_from, password, email_to, message):
    print(email_from)
    print(password)
    print(email_to)
    print(message)
    
    
    msg = email.message.Message()
    msg['Subject'] = 'Automatic'
    msg['From'] = email_from
    msg['To'] = remetente
    password = password 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message)

    try:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except:
        print('Falha na Operação')


informacoes = Lendo_ini()

while True: 
    message = input('Insira sua mensagem : ')
    remetente = input('Insira e-mail remetente : ')
    enviar_email(informacoes.email, informacoes.password, remetente, message)
#print(informacoes.email, informacoes.password)


