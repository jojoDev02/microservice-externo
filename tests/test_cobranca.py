import unittest
from unittest.mock import Mock
from src.core.use_cases.incluir_cobranca import IncluirCobrancaNaFilaUseCase  # Substitua 'seu_modulo' pelo nome do módulo que contém o código fornecido
from core.models.cobranca import Cobranca

class TestIncluirCobrancaNaFilaUseCase(unittest.TestCase):

    def test_execute_inclusao_sucesso(self):
   
        fila_service_mock = Mock()
        incluir_cobranca_use_case = IncluirCobrancaNaFilaUseCase(fila_service_mock)
        cobranca = Cobranca()  # Pode ajustar conforme necessário

  
        fila_service_mock.incluir.return_value = True
        result = incluir_cobranca_use_case.execute(cobranca)

    
        fila_service_mock.incluir.assert_called_once_with(cobranca)
        cobranca.set_horario_finalizacao.assert_called_once()
        self.assertTrue(result)

    def test_execute_inclusao_falha(self):
    
        fila_service_mock = Mock()
        incluir_cobranca_use_case = IncluirCobrancaNaFilaUseCase(fila_service_mock)
        cobranca = Cobranca()  # Pode ajustar conforme necessário

      
        fila_service_mock.incluir.return_value = False
        result = incluir_cobranca_use_case.execute(cobranca)


        fila_service_mock.incluir.assert_called_once_with(cobranca)
        cobranca.set_horario_finalizacao.assert_not_called()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
