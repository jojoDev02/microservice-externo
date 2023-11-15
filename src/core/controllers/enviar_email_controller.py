from email_validator import validate_email
from core.models.email import Email
from core.use_cases.enviar_email import EnviarEmailUseCase


class EnviarEmailController:

    def __init__(self, use_case: EnviarEmailUseCase) -> None:
        self.__use_case = use_case

    def enviar_email(self, destinatario: str, assunto: str, mensagem: str):
            
            try: 
                validate_email(destinatario)
            except:
                return {
                    "codigo" : "422",
                    "mensagem" : "E-mail com formato inválido"
                }, 422
     
            email = Email(destinatario, assunto, mensagem)
            resultado = self.__use_case.execute(email)

            if resultado:
                return email.to_dict(), 200
            else:
                return {
                    "codigo" : "422",
                    "mensagem" : "E-mail não existe"
                }, 404  
        
      
        