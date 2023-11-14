import random
from flask import Flask
from flask_mail import Mail, Message
from core.interfaces.enivar_email import EmailServiceInterface

# Implementacao concreta do envio de email
class EmailService(EmailServiceInterface):
    # def __init__(self, app: Flask) -> None:
    #     self.mail = Mail(app)

    def enviar_email(self, destinatario: str, assunto: str, mensagem: str) -> None:

        return random.choice([True, False])
    