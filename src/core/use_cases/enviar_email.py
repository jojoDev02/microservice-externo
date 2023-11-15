from core.models.email import Email
from core.interfaces.enivar_email import EmailServiceInterface

# Camada de serviço que depende apenas da interface
class EnviarEmailUseCase:

    def __init__(self, email_service: EmailServiceInterface):
        self.email_service = email_service

    def execute(self, email: Email) -> None:
        # Lógica de negócios para o envio de e-mail
       
            enviado = self.email_service.enviar_email(email)

            return enviado
        

# As regras de negocios sao implementadas aqui, erros tambem são tratados nessa camada

