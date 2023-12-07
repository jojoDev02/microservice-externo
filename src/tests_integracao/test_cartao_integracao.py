import os
import sys
import unittest
from flask import Flask


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


from external.api.cartao import cartao_bp

class TestValidaCartaoIntegration(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(cartao_bp)
        self.client = self.app.test_client()

    def test_valida_cartao(self):
        # Dados de exemplo
        dados_cartao = {
            "nomeTitular": "Teste",
            "numero": "1234567890123456",
            "validade": "2023-12-13",
            "cvv": "7937"
        }

        # Envia uma requisição POST para a rota
        response = self.client.post('/validaCartaoDeCredito', json=dados_cartao)
        print(response.status_code)
        print(response)
        # Verifica se a resposta está correta
        self.assertEqual(response.status_code, 200)


    def test_valida_cartao_invalido(self):
            # Dados de exemplo inválidos
            dados_cartao_invalido = {
                "nomeTitular": "Teste",
                "numero": "invalido",  # Número inválido de propósito
                "validade": "2023-12-13",
                "cvv": "7937"
            }

            # Envia uma requisição POST para a rota com dados inválidos
            response = self.client.post('/validaCartaoDeCredito', json=dados_cartao_invalido)

            # Verifica se a resposta está correta para dados inválidos
            self.assertEqual(response.status_code, 422)

            # Verifica o conteúdo da resposta para dados inválidos
            resultado = response.get_json()

if __name__ == '__main__':
    unittest.main()
