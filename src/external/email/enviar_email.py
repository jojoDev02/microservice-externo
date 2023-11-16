from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import config
import smtplib
from core.interfaces.enivar_email import EmailServiceInterface
from core.models.email import Email

# Implementacao concreta do envio de email
class EmailService(EmailServiceInterface):
    def __init__(self) -> None:
        self.host = config.MAIL_SERVER 
        self.port = config.MAIL_PORT 
        self.username = config.MAIL_USERNAME
        self.password = config.MAIL_PASSWORD

    def enviar_email(self, email: Email) -> bool:
        # Cria uma conexão com o servidor SMTP
        servidor = smtplib.SMTP(self.host, self.port)

        # Autentica-se no servidor
        servidor.starttls()
        servidor.login(self.username, self.password)

        # Cria a mensagem de e-mail
        mensagem = MIMEMultipart()
        mensagem['From'] = 'jordanafcavalcante@gmail.com'
        mensagem['To'] = email.destinatario
        mensagem['Subject'] = email.assunto

        body = MIMEText(email.mensagem, 'plain')
        mensagem.attach(body)

        # Envia a mensagem de e-mail
        servidor.send_message(mensagem)

        # Fecha a conexão com o servidor
        servidor.quit()

        return True
    

    