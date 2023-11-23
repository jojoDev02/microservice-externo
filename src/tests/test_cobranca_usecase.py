import os
import sys
import unittest
from unittest.mock import Mock, patch
import uuid




# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)
from core.interfaces.fila_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca
from core.use_cases.obter_cobranca import ObterCobrancaUseCase
from core.use_cases.incluir_cobranca import IncluirCobrancaNaFilaUseCase
from core.use_cases.processar_cobrancas import ProcessarCobrancasUseCase

class TestCobrancaUseCase(unittest.TestCase):

    def test_obter_cobranca_sucesso(self):
        cobranca = Cobranca(100.0, 4)

        
        mock_fila = Mock(spec=FilaCobrancaInterface)

        use_case = ObterCobrancaUseCase(mock_fila)

        mock_fila.obter_cobranca.return_value = cobranca

        cobranca_retornada = use_case.execute(cobranca.id)

        mock_fila.obter_cobranca.called_once_with(cobranca.id)

        self.assertEqual(cobranca_retornada, cobranca)

    def test_obter_cobranca_falha(self):
        cobranca_id = str(uuid.uuid4())

        mock_fila = Mock(spec=FilaCobrancaInterface)

        mock_fila.obter_cobranca.return_value = None
        
        use_case = ObterCobrancaUseCase(mock_fila)

        cobranca_retornada = use_case.execute(cobranca_id)

        mock_fila.obter_cobranca.called_once_with(cobranca_id)

        self.assertIsNone(cobranca_retornada)

    def test_incluir_cobranca_sucesso(self):
        mock_fila_service = Mock(spec=FilaCobrancaInterface)
        use_case = IncluirCobrancaNaFilaUseCase(mock_fila_service)
        # Configurar o mock para retornar True (simulando inclusão bem-sucedida na fila)
        cobranca_mock = Mock(spec=Cobranca)
        mock_fila_service.incluir.return_value = True

        # Chamar o método que você deseja testar
        resultado = use_case.execute(cobranca_mock)

        # Verificar se o método da fila foi chamado corretamente
        mock_fila_service.incluir.assert_called_once_with(cobranca_mock)

        # Verificar o resultado em caso de sucesso
        self.assertTrue(resultado)

    def test_incluir_cobranca_falha(self):
        mock_fila_service = Mock(spec=FilaCobrancaInterface)
        use_case = IncluirCobrancaNaFilaUseCase(mock_fila_service)
        # Configurar o mock para retornar False (simulando falha na inclusão na fila)
        cobranca_mock = Mock(spec=Cobranca)
        mock_fila_service.incluir.return_value = False

        # Chamar o método que você deseja testar
        resultado = use_case.execute(cobranca_mock)

        # Verificar se o método da fila foi chamado corretamente
        mock_fila_service.incluir.assert_called_once_with(cobranca_mock)

        # Verificar o resultado em caso de falha
        self.assertFalse(resultado)

    def test_processar_cobrancas_usecase(self):
        mock_fila_cobranca = Mock(spec=FilaCobrancaInterface)
        use_case = ProcessarCobrancasUseCase(mock_fila_cobranca)
        # Configurar o mock para retornar uma lista simulada de cobranças processadas
        cobranca_mock_1 = Mock()
        cobranca_mock_2 = Mock()
        mock_fila_cobranca.processar_cobrancas.return_value = [cobranca_mock_1, cobranca_mock_2]

        # Chamar o método que você deseja testar
        result = use_case.execute()

        # Verificar se o método da fila foi chamado corretamente
        mock_fila_cobranca.processar_cobrancas.assert_called_once()

        # Verificar o resultado
        self.assertEqual(result, [cobranca_mock_1, cobranca_mock_2])

    def test_processar_cobrancas_usecase_falha(self):
        mock_fila_cobranca = Mock(spec=FilaCobrancaInterface)
        use_case = ProcessarCobrancasUseCase(mock_fila_cobranca)
            # Configurar o mock para retornar uma lista vazia simulando falha no processamento
        mock_fila_cobranca.processar_cobrancas.return_value = []

        # Chamar o método que você deseja testar
        result = use_case.execute()

        # Verificar se o método da fila foi chamado corretamente
        mock_fila_cobranca.processar_cobrancas.assert_called_once()

        # Verificar o resultado em caso de falha
        self.assertEqual(result, [])