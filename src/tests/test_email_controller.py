
# Obtém o caminho absoluto para o diretório raiz do projeto
import os
import sys


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)


import unittest
from unittest.mock import Mock, patch
from core.models.email import Email
from core.use_cases.enviar_email import EnviarEmailUseCase
from controllers.enviar_email_controller import EnviarEmailController

class TestEnviarEmailController(unittest.TestCase):

    @patch('controllers.enviar_email_controller.EnviarEmailUseCase')
    def test_enviar_email(self, mock_use_case):
     
        # Configuração do mock de EnviarEmailUseCase
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = True

        # Criação da instância da classe controller com os mocks como dependências
        controller = EnviarEmailController(mock_instance)

        # Chamada do método a ser testado
        result, status_code = controller.enviar_email("destinatario@test.com", "Assunto", "Mensagem")

        mock_instance.execute.assert_called_once() 

        mock_instance.execute.assert_called_once()

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 200)
        self.assertEqual(result, Email("destinatario@test.com", "Assunto", "Mensagem").to_dict())

    @patch('controllers.enviar_email_controller.EnviarEmailUseCase')
    def test_enviar_email_com_falha(self, mock_use_case):
        # Configuração do mock de EnviarEmailUseCase para simular falha
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = False

        # Criação da instância da classe controller com os mocks como dependências
        controller = EnviarEmailController(mock_instance)

        # Chamada do método a ser testado
        result, status_code = controller.enviar_email("destinatario@test.com", "Assunto", "Mensagem")

        # Asserts para verificar interação com mocks
        mock_instance.execute.assert_not_called()  # Não deveria ter sido chamado devido à falha na validação

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 422)
        self.assertEqual(result, {
            "codigo": "422",
            "mensagem": "E-mail com formato inválido"
        })

if __name__ == '__main__':
    unittest.main()
