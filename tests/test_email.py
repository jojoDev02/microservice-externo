import unittest, os , sys
from unittest.mock import  patch


from src.core.use_cases.enviar_email import EnviarEmailUseCase


class EmailTeste(unittest.TestCase):

    @patch('src.core.models.email.Email')
    @patch('src.core.use_cases.enviar_email.EmailServiceInterface')
    def test_enviar(self,mock_email,  mock_enviar_email_interface):
        

        mock_enviar_email_interface.enviar_email.return_value = True

        use_case = EnviarEmailUseCase()

        use_case.execute(mock_email)

        mock_enviar_email_interface.enviar_email.assert_called_once()

    if __name__ == "__main__":
        unittest.main()


