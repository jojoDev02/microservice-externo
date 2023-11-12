from abc import ABC, abstractmethod

# Defina uma interface para o serviço de e-mail
class EmailServiceInterface(ABC):
    @abstractmethod
    def enviar_email(self, destinatario: str, assunto: str, mensagem: str) -> bool: pass


