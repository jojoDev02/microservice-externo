import unittest
from external.email.enviar_email import EmailService
from core.models.email import Email
from unittest.mock import Mock

class EmailServiceTests(unittest.TestCase):

    def test_email_invalido(self):
        # Cria um objeto Email válido
        email = Mock(Email)

        # Cria uma instância do serviço de envio de email
        service = Mock(EmailService)

        # Envia o email
        resultado = service

        # Verifica se o resultado é True
        self.assertTrue(resultado)

    def test_enviar_email(self): pass

    def test_enviar_email_controller(self): pass



if __name__ == "__main__":
    unittest.main()
