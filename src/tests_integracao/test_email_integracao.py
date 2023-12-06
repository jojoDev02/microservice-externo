import os
import sys
import unittest
from unittest.mock import Mock



project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controllers.enviar_email_controller import EnviarEmailController
from core.use_cases.enviar_email import EnviarEmailUseCase
from external.email.enviar_email import EmailService


class TestEnviarEmailController(unittest.TestCase):

    def setUp(self):
        # Configurar o mock para o caso de uso
        self.enviar_email_service = EmailService()
        self.enviar_email_use_case= EnviarEmailUseCase(self.enviar_email_service)
        self.enviar_email_controller = EnviarEmailController(self.enviar_email_use_case)

    def test_enviar_email_sucesso(self):
        destinatario = "jordana.cavalcante@edu.unirio.br"
        assunto = "Assunto do Email"
        mensagem = "Conteúdo do Email"

        response, status_code = self.enviar_email_controller.enviar_email(destinatario, assunto, mensagem)

        self.assertEqual(status_code, 200)
        self.assertIsNotNone(response)


    def test_enviar_email_formato_invalido(self):
        # Testar o caso em que o e-mail tem um formato inválido
        destinatario_invalido = "destinatario.invalido"  # Um endereço de e-mail inválido
        response, status_code = self.enviar_email_controller.enviar_email(destinatario_invalido, "Assunto", "Mensagem")

        # Verificar se o código de status e a mensagem de erro são os esperados
        self.assertEqual(status_code, 422)
        self.assertEqual(response["codigo"], "422")
        self.assertEqual(response["mensagem"], "E-mail com formato inválido")

if __name__ == '__main__':
    unittest.main()