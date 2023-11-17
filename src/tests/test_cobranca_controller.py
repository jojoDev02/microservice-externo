import os
import sys
import unittest
from unittest.mock import Mock, patch

# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)

from controllers.processar_cobranca_controller import ProcessarCobrancasController

class TestProcessarCobrancasController(unittest.TestCase):


    @patch('core.use_cases.processar_cobrancas.ProcessarCobrancasUseCase')
    def test_processar_cobrancas(self, mock_use_case):
        # Criação de instância do mock para ProcessarCobrancasUseCase
        mock_instance = mock_use_case.return_value
        # Configuração do comportamento do mock
        mock_instance.execute.return_value = [mock_cobranca()]

        # Criação da instância da classe controller com o mock como dependência
        controller = ProcessarCobrancasController(mock_instance)

        # Chamada do método a ser testado
        result, status_code = controller.processar_cobrancas()

        # Asserts para verificar se o método interagiu corretamente com o mock
        mock_instance.execute.assert_called_once() 

        # Asserts para verificar o resultado retornado pelo método
        self.assertEqual(status_code, 200)
        self.assertEqual(result, [mock_cobranca().to_dict()])

# Função auxiliar para criar um mock de cobrança
def mock_cobranca():
    cobranca = Mock()
    cobranca.to_dict.return_value = {'campo1': 'valor1', 'campo2': 'valor2'}
    return cobranca

if __name__ == '__main__':
    unittest.main()
