from abc import ABC, abstractmethod

from core.models.email import Email

# Defina uma interface para o serviço de e-mail
class EmailServiceInterface(ABC):
    @abstractmethod
    def enviar_email(self, email: Email) -> bool: pass


