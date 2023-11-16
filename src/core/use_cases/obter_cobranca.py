from core.interfaces.fila_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca

#implementa o caso de uso de inclusao na fila de cobranças
class ObterCobrancaUseCase:

    def __init__(self, fila_service: FilaCobrancaInterface) -> None:
        self.fila = fila_service
    
    def execute(self, cobranca_id) -> Cobranca:
        return self.fila.obter_cobranca(cobranca_id)

       