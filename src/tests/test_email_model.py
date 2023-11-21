import os
import sys
import unittest
from uuid import uuid4
# Obtém o caminho absoluto para o diretório raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)

from core.models.email import Email


class EmailTest(unittest.TestCase):

    def test_init(self):
        destinatario = "joao@silva.com"
        assunto = "Assunto do e-mail"
        mensagem = "Mensagem do e-mail"

        email = Email(destinatario, assunto, mensagem)

        self.assertIsInstance(email, Email)
        self.assertIsNotNone(email.id)
        self.assertEqual(email.destinatario, destinatario)
        self.assertEqual(email.assunto, assunto)
        self.assertEqual(email.mensagem, mensagem)

    def test_to_dict(self):
        destinatario = "joao@silva.com"
        assunto = "Assunto do e-mail"
        mensagem = "Mensagem do e-mail"

        email = Email(destinatario, assunto, mensagem)
        email_dict = email.to_dict()

        self.assertEqual(email_dict['destinatario'], destinatario)
        self.assertEqual(email_dict['assunto'], assunto)
        self.assertEqual(email_dict['mensagem'], mensagem)


