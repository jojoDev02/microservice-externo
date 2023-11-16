import unittest, os , sys
from unittest.mock import Mock, patch
from src.core.models.email import Email
from src.core.use_cases.enviar_email import EnviarEmailUseCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

class EmailTeste(unittest.TestCase):
    
    @patch('core.use_cases.enviar_email.EmailServiceInterface')
    def test_enviar(self, mock_enviar_email_interface):
        email = Mock(Email)

        mock_enviar_email_interface().enviar_email.return_value = True

        use_case = EnviarEmailUseCase()

        use_case.execute(email)

        mock_enviar_email_interface().enviar_email.assert_called_once()

    

if __name__ == "__main__":
    unittest.main()


