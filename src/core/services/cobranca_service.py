from core.interfaces.incluir_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca
from core.models.fila_cobranca import FilaCobranca

# implementa a funcionalidade de acesso a dados da fila de cobrança
class CobrancaService(FilaCobrancaInterface):

    def __init__(self, fila: FilaCobranca) -> None:
        self.fila = fila

    def incluir(self, cobranca: Cobranca) -> None:
        if cobranca.status != "PAGA" :
            self.fila.add_cobranca(cobranca)
            return True
        

#posso fazer outra manipulacoes de dados aqui 