import os
import sys
import unittest
from unittest.mock import Mock, patch

# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)
from core.models.cartao_credito import CartaoCredito
from controllers.validar_cartao_controller import ValidarCartaoController

class TestValidarCartaoController(unittest.TestCase):

    @patch('controllers.validar_cartao_controller.ValidarCartaoUseCase')
    def test_validar_cartao_sucesso(self, mock_use_case):
        # Configuração do mock de ValidarCartaoUseCase para simular sucesso
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = True

        # Criação da instância da classe controller com o mock como dependência
        controller = ValidarCartaoController(mock_instance)

        # Chamada do método a ser testado
        result, status_code = controller.validar_cartao("Titular", "1234567890123456", "12/25", "1235")

        # Asserts para verificar interação com o mock
        mock_instance.execute.assert_called_once() 

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 200)
        self.assertEqual(result, {
            "codigo": "200",
            "mensagem": "Dados atualizados!"
        })


    @patch('controllers.validar_cartao_controller.ValidarCartaoUseCase')
    def test_validar_cartao_falha(self, mock_use_case):
        # Configuração do mock de ValidarCartaoUseCase para simular falha
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = False

        # Criação da instância da classe controller com o mock como dependência
        controller = ValidarCartaoController(mock_instance)

        # Chamada do método a ser testado
        result, status_code = controller.validar_cartao("Titular", "invalid_number", "12/25", "123")

        # Asserts para verificar interação com o mock
        mock_instance.execute.assert_called_once() 

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 422)
        self.assertEqual(result, {
            "codigo": "422",
            "mensagem": "Dados Inválidos!"
        })

if __name__ == '__main__':
    unittest.main()
