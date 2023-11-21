import os
import sys
import unittest
from unittest.mock import Mock, patch

# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)
from controllers.incluir_cobranca import IncluirCobrancaController


class TestIncluirCobrancaController(unittest.TestCase):

    @patch('controllers.incluir_cobranca.IncluirCobrancaNaFilaUseCase')
    def testa_inclusao_sucesso_cobranca(self, mock_use_case):
        # Configuração do mock de IncluirCobrancaNaFilaUseCase para simular sucesso
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = True

        # Criação da instância da classe controller com o mock como dependência
        controller = IncluirCobrancaController(mock_instance)

        # Chamada do método a ser testado
        resposta, status_code = controller.incluir_cobranca(100.0, 4)

        # Asserts para verificar interação com o mock
        mock_instance.execute.assert_called_once()

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 200)
     

    @patch('controllers.incluir_cobranca.IncluirCobrancaNaFilaUseCase')
    def testa_inclusao_falha_cobranca(self, mock_use_case):
        # Configuração do mock de IncluirCobrancaNaFilaUseCase para simular falha
        mock_instance = mock_use_case.return_value
        mock_instance.execute.return_value = False

        # Criação da instância da classe controller com o mock como dependência
        controller = IncluirCobrancaController(mock_instance)

        # Chamada do método a ser testado
        resposta, status_code = controller.incluir_cobranca(100.0, 4)

        # Asserts para verificar interação com o mock
        mock_instance.execute.assert_called_once()

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 422)

        self.assertEqual(resposta, {
            "codigo": "422",
            "mensagem": "Dados Inválidos!"
        })

if __name__ == '__main__':
    unittest.main()
