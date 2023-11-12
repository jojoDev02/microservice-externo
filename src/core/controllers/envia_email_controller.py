
from core.models.email import Email
from core.use_cases.enviar_email import EnviarEmailUseCase


class EnviarEmailController:

    def __init__(self, use_case: EnviarEmailUseCase) -> None:
        self.__use_case = use_case

    def enviar_email(self, destinatario: str, assunto: str, mensagem: str):
        try:
            email = Email(destinatario, assunto, mensagem)
            self.__use_case.execute(email)
            return "E-mail enviado com sucesso!", 200
        
        except Exception as e:
            return f"Erro ao enviar e-mail: {str(e)}", 500
