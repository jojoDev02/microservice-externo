from core.interfaces.fila_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca

#implementa o caso de uso de inclusao na fila de cobranças
class IncluirCobrancaNaFilaUseCase:

    def __init__(self, fila_service: FilaCobrancaInterface) -> None:
        self.fila = fila_service

    
    def execute(self, cobranca: Cobranca ) -> bool:
        incluiu = self.fila.incluir(cobranca)
        if incluiu:
            cobranca.set_horario_finalizacao()
            return True
        
       