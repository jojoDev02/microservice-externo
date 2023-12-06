import json
import os
import sys
import unittest
from flask import Flask

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from external.api.cobranca import cobranca_bp 

class TestCobrancaEndpoints(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(cobranca_bp)
        self.app = app.test_client()

    def test_realizar_cobranca_endpoint(self):
        data = {
            "valor": 100.0,
            "ciclista": 2
        }
        response = self.app.post('/cobranca', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.get_data(as_text=True))

    def test_incluir_cobranca_endpoint(self):
        data = {
            "valor": 50.0,
            "ciclista": 1
        }
        response = self.app.post('/filaCobranca', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.get_data(as_text=True))

    def test_get_cobranca_endpoint_404(self):
        response = self.app.get('/cobranca/b382d7af-337f-4814-bd8b-bd4f8ecfd57b')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.get_data(as_text=True))


    def test_processa_cobrancas_endpoint(self):
        response = self.app.post('/processaCobrancasEmFila')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
