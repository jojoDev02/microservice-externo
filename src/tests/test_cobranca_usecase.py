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
