import os
import sys
import unittest
from collections import deque
from queue import Queue
import uuid
from unittest.mock import Mock, patch


# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)

from core.models.cobranca import Cobranca
from core.models.fila_cobranca import FilaCobranca

class FilaCobrancaTest(unittest.TestCase):

    def test_get_cobranca(self):
        cobranca = Cobranca(100.0, 4)

        fila_cobranca = FilaCobranca()

        fila_cobranca.add_cobranca(cobranca)

        resultado = fila_cobranca.get_cobranca(str(cobranca.id))

        self.assertEqual(resultado, cobranca)

    def test_get_cobranca_falha(self):
        cobranca = Cobranca(100.0, 4)

        fila_cobranca = FilaCobranca()

        resultado = fila_cobranca.get_cobranca(str(cobranca.id))

        self.assertIsNone(resultado)

    def test_add_cobranca(self):
        cobranca = Mock(spec=Cobranca)

        fila_cobranca = FilaCobranca()
       
        fila_cobranca.add_cobranca(cobranca)

        self.assertEqual(len(fila_cobranca.fila), 1)

    def test_retira_cobranca(self):
        cobranca = Mock(spec=Cobranca)

        fila_cobranca = FilaCobranca()

        fila_cobranca.add_cobranca(cobranca)

        cobranca_retirada = fila_cobranca.retira_cobranca()

        self.assertEqual(cobranca_retirada, cobranca)
        self.assertEqual(len(fila_cobranca.fila), 0)

    def test_retira_cobranca_empty(self):

        fila_cobranca = FilaCobranca()
        cobranca_retirada = fila_cobranca.retira_cobranca()

        self.assertIsNone(cobranca_retirada)
        self.assertEqual(len(fila_cobranca.fila), 0)

    def test_get_all_cobrancas(self):
        cobranca1 = Mock(spec=Cobranca)
        cobranca2 = Mock(spec=Cobranca)
        
        fila_cobranca = FilaCobranca()

        fila_cobranca.add_cobranca(cobranca1)
        fila_cobranca.add_cobranca(cobranca2)

        cobrancas = fila_cobranca.get_all_cobrancas()
        
        self.assertEqual(list(cobrancas), [cobranca1, cobranca2])

    def test_get_all_cobrancas_empty(self):
        
        fila_cobranca = FilaCobranca()
        
        cobrancas = fila_cobranca.get_all_cobrancas()
        
        self.assertEqual(list(cobrancas), [])