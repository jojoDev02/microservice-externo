import os
import sys
import unittest
from datetime import datetime
from uuid import uuid4
from enum import Enum, auto

# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)

from core.models.cobranca import Cobranca
from core.models.cobranca import StatusCobranca


class TestCobrancaModel(unittest.TestCase):

    def test_init(self):
        valor = 100.0
        ciclista = 4
        cobranca = Cobranca(valor, ciclista)

        self.assertIsInstance(cobranca, Cobranca)
        self.assertIsNotNone(cobranca.id)
        self.assertEqual(cobranca.status, StatusCobranca.PENDENTE.name)
        self.assertIsNotNone(cobranca.hora_solicitacao)
        self.assertIsNone(cobranca.hora_finalizacao)
        self.assertEqual(cobranca.valor, valor)
        self.assertEqual(cobranca.ciclista, ciclista)

    def test_marcar_como_incluida(self):
        cobranca = Cobranca(100.0, 4)
        cobranca.marcar_como_incluida()

        self.assertIsNotNone(cobranca.hora_finalizacao)

    def test_marcar_como_falha(self):
        cobranca = Cobranca(100.0, 4)
        cobranca.marcar_como_falha()

        self.assertEqual(cobranca.status, StatusCobranca.FALHA.name)

    def test_marcar_como_paga(self):
        cobranca = Cobranca(100.0, 4)
        cobranca.marcar_como_paga()

        self.assertEqual(cobranca.status, StatusCobranca.PAGA.name)
        self.assertIsNotNone(cobranca.hora_finalizacao)

    def test_get_status(self):
        cobranca = Cobranca(100.0, 4)
        self.assertEqual(cobranca.get_status(), StatusCobranca.PENDENTE.name)

        cobranca.marcar_como_paga()
        self.assertEqual(cobranca.get_status(), StatusCobranca.PAGA.name)

    def test_to_dict(self):
        cobranca = Cobranca(100.0, 4)
        cobranca_dict = cobranca.to_dict()

        self.assertEqual(cobranca_dict['id'], cobranca.id)
        self.assertEqual(cobranca_dict['status'], cobranca.status)
        self.assertEqual(cobranca_dict['horaSolicitacao'], cobranca.hora_solicitacao)
        self.assertEqual(cobranca_dict['horaFinalizacao'], cobranca.hora_finalizacao)
        self.assertEqual(cobranca_dict['valor'], cobranca.valor)
        self.assertEqual(cobranca_dict['ciclista'], cobranca.ciclista)
