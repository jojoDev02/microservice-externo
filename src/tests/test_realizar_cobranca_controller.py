import os
import sys
import unittest
from unittest.mock import Mock

# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)
from core.models.cobranca import Cobranca
from core.use_cases.realizar_cobranca import RealizarCobrancaUseCase
from controllers.realizar_cobranca import RealizarCobrancaController

class TestRealizarCobrancaController(unittest.TestCase):

    def setUp(self):
        # Configurar mocks para as dependências
        self.mock_use_case = Mock(spec=RealizarCobrancaUseCase)
        self.controller = RealizarCobrancaController(self.mock_use_case)

    def test_realizar_cobranca_sucesso(self):
        # Configurar o mock para o sucesso do use_case.execute()
        cobranca_mock = Mock(spec=Cobranca)
        self.mock_use_case.execute.return_value = True

        # Chamar o método que você deseja testar
        result, status_code = self.controller.realizar_cobranca(valor=100, ciclista=4)

        # Verificar se o método do use_case foi chamado corretamente
        self.mock_use_case.execute.assert_called_once()

        # Verificar o resultado em caso de sucesso
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(result, cobranca_mock)

    def test_realizar_cobranca_falha(self):
        # Configurar o mock para a falha do use_case.execute()
        cobranca_mock = Mock(spec=Cobranca)
        self.mock_use_case.execute.return_value = False

        # Chamar o método que você deseja testar
        result, status_code = self.controller.realizar_cobranca(valor=100, ciclista='João')

        # Verificar se o método do use_case foi chamado corretamente
        self.mock_use_case.execute.assert_called_once()

        # Verificar o resultado em caso de falha
        self.assertEqual(status_code, 422)
        self.assertEqual(result, {"codigo": "422", "mensagem": "Falha no processamento"})

if __name__ == '__main__':
    unittest.main()
