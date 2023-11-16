import unittest
from unittest.mock import Mock
from core.use_cases.processar_cobrancas import ProcessarCobrancasUseCase
from src.core.use_cases.obter_cobranca import ObterCobrancaUseCase
from core.models.cobranca import Cobranca

class TestObterCobrancaUseCase(unittest.TestCase):

    def test_execute_sucesso(self):
       
        fila_service_mock = Mock()
        obter_cobranca_use_case = ObterCobrancaUseCase(fila_service_mock)
        cobranca_id = 1  
        cobranca_retorno = Cobranca(id=cobranca_id) 

 
        fila_service_mock.obter_cobranca.return_value = cobranca_retorno
        result = obter_cobranca_use_case.execute(cobranca_id)

       
        fila_service_mock.obter_cobranca.assert_called_once_with(cobranca_id)
        self.assertEqual(result, cobranca_retorno)

    def test_execute_cobranca_nao_encontrada(self):
        
        fila_service_mock = Mock()
        obter_cobranca_use_case = ObterCobrancaUseCase(fila_service_mock)
        cobranca_id = 2 

       
        fila_service_mock.obter_cobranca.return_value = None
        result = obter_cobranca_use_case.execute(cobranca_id)

       
        fila_service_mock.obter_cobranca.assert_called_once_with(cobranca_id)
        self.assertIsNone(result)

    class TestProcessarCobrancasUseCase(unittest.TestCase):

        def test_execute(self):
            # Arrange
            fila_cobranca_mock = Mock()
            processar_cobrancas_use_case = ProcessarCobrancasUseCase(fila_cobranca_mock)
            cobrancas_processadas_mock = ['cobranca1', 'cobranca2']  # Pode ajustar conforme necessário

            # Act
            fila_cobranca_mock.processar_cobrancas.return_value = cobrancas_processadas_mock
            result = processar_cobrancas_use_case.execute()

            # Assert
            fila_cobranca_mock.processar_cobrancas.assert_called_once()
            self.assertEqual(result, cobrancas_processadas_mock)

if __name__ == '__main__':
    unittest.main()
