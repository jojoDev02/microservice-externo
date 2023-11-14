
from core.models.email import Email
from core.use_cases.enviar_email import EnviarEmailUseCase


class EnviarEmailController:

    def __init__(self, use_case: EnviarEmailUseCase) -> None:
        self.__use_case = use_case

    def enviar_email(self, destinatario: str, assunto: str, mensagem: str):
     
            email = Email(destinatario, assunto, mensagem)
            resultado = self.__use_case.execute(email)

            if resultado:
                return {
                    "codigo" : "200",
                    "mensagem" : "E-mail enviado com sucesso!"
                }, 200
            else:
                return {
                    "codigo" : "422",
                    "mensagem" : "E-mail não existe"
                }, 404

                # return {
                #     "codigo" : "422",
                #     "mensagem" : "E-mail com formato inválido"
                # }, 422

# depois arrumar o tratamento de erros     
        
      
        