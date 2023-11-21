import os
import sys
import unittest
from unittest.mock import Mock, patch



# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)

from core.models.cobranca import Cobranca, StatusCobranca
from core.models.fila_cobranca import FilaCobranca
from core.services.fila_cobranca_service import FilaCobrancaService

class TestFilaCobrancaService(unittest.TestCase):

    def test_incluir_cobranca_sucesso(self):
        # Cria um mock para a classe FilaCobranca
        mock_fila = Mock(spec=FilaCobranca)

        # Cria uma instância do serviço de fila de cobrança
        service = FilaCobrancaService(mock_fila)
        
        # Chama o método a ser testado
        service.incluir(Cobranca(100, 4))

        # Valida a interação com o mock
        mock_fila.add_cobranca.assert_called_once()


    def test_incluir_cobranca_falha(self):
        # Cria um mock para a classe FilaCobranca
        mock_fila = Mock(spec=FilaCobranca)

        # Cria uma instância do serviço de fila de cobrança
        service = FilaCobrancaService(mock_fila)

        # Chama o método a ser testado
        service.incluir(Cobranca(100.0, 4))

        # Valida a interação com o mock
        mock_fila.add_cobranca.assert_called_once()


    def testa_obter_cobranca_sucesso(self):
 
        mock_fila = Mock(spec=FilaCobranca)

        service = FilaCobrancaService(mock_fila)

        cobranca = service.obter_cobranca(1)

        mock_fila.get_cobranca.assert_called_once()
   
        self.assertIsNotNone(cobranca)
        

    def testa_obter_cobranca_falha(self):

        mock_fila = Mock(spec=FilaCobranca)

        mock_fila.get_cobranca.return_value = None
 
        cobranca = mock_fila.get_cobranca(1)

        self.assertIsNone(cobranca)


if __name__ == '__main__':
    unittest.main()
