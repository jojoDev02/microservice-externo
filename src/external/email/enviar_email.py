from flask import Flask
from flask_mail import Mail, Message
from core.interfaces.enivar_email import EmailServiceInterface

# Implementacao concreta do envio de email
class EmailService(EmailServiceInterface):
    # def __init__(self, app: Flask) -> None:
    #     self.mail = Mail(app)

    def enviar_email(self, destinatario: str, assunto: str, mensagem: str) -> None:
        # try:
        #     msg = Message(
        #         subject=assunto,
        #         recipients=[destinatario],
        #         body=mensagem
        #     )
        #     self.mail.send(msg)
        #     return 
        
        # except Exception as e:
        #     raise Exception(e)
        return