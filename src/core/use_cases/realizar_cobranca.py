from core.models.cobranca import Cobranca
from core.interfaces.realizar_cobranca import ProcessadorCobrancaInterface
class RealizarCobrancaUseCase:

    def __init__(self, processador_cobranca: ProcessadorCobrancaInterface) -> None:
        self.processador_cobranca = processador_cobranca

    def execute(self, cobranca: Cobranca):
            
            efetuada = self.processador_cobranca.efetuar(cobranca)

            if efetuada:
                cobranca.marcar_como_paga()
            else:
                cobranca.marcar_como_falha()
            
            return efetuada
         