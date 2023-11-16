import unittest, os , sys
from unittest.mock import Mock, patch
from src.core.models.email import Email
from src.core.use_cases.enviar_email import EnviarEmailUseCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

class EmailTeste(unittest.TestCase):
    
    @patch('core.use_cases.enviar_email.EmailServiceInterface')
    def test_enviar(self, mock_enviar_email_interface):
        # Cria um objeto Email válido
        email = Mock(Email)

        # Configura o retorno esperado do método enviar_email na interface
        mock_enviar_email_interface().enviar_email.return_value = True

        # Cria uma instância do serviço de envio de email
        use_case = EnviarEmailUseCase()

        # Chama o método `execute`
        use_case.execute(email)

        # Verifica se o método `enviar_email` foi chamado
        mock_enviar_email_interface().enviar_email.assert_called_once()

        # Verifica se o método `enviar_email` foi chamado com o email correto
        mock_enviar_email_interface().enviar_email.assert_called_with(email)

if __name__ == "__main__":
    unittest.main()


