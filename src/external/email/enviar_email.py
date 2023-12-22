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
        self.host = os.environ.get("MAIL_SERVER") 
        self.port = os.environ.get("MAIL_PORT") 
        self.username = os.environ.get("MAIL_USERNAME") 
        self.password = os.environ.get("MAIL_PASSWORD") 

    def enviar_email(self, email: Email) -> bool:
        # Cria uma conexão com o servidor SMTP
        servidor = smtplib.SMTP(self.host, self.port)

        # Autentica-se no servidor
        servidor.starttls()
        servidor.login(self.username, self.password)

        # Cria a mensagem de e-mail
        mensagem = MIMEMultipart()
        mensagem['From'] = 'exemplo@gmail.com'
        mensagem['To'] = email.destinatario
        mensagem['Subject'] = email.assunto

        body = MIMEText(email.mensagem, 'plain')
        mensagem.attach(body)

        # Envia a mensagem de e-mail
        servidor.send_message(mensagem)

        # Fecha a conexão com o servidor
        servidor.quit()

        return True
    

    
