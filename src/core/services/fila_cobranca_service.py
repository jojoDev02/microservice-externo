import uuid
from core.interfaces.fila_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca
from core.models.fila_cobranca import FilaCobranca

# implementa a funcionalidade de acesso a dados da fila de cobrança
class FilaCobrancaService(FilaCobrancaInterface):

    def __init__(self, fila: FilaCobranca) -> None:
        self.fila = fila

    def incluir(self, cobranca: Cobranca) -> bool:
        if cobranca.status != "PAGA" :
            self.fila.add_cobranca(cobranca)
            return True
    
    def processar_cobrancas(self) -> list: 

        cobrancas_pagas = []

        for cobranca in self.fila.get_all_cobrancas():
               
                if cobranca.marcar_como_paga():
                    cobrancas_pagas.append(cobranca)
           
        return cobrancas_pagas

    def obter_cobranca(self, cobranca_id):
        cobranca = self.fila.get_cobranca(cobranca_id)
        return cobranca
            
    
      
