from core.interfaces.fila_cobranca import FilaCobrancaInterface
from core.models.cobranca import Cobranca, StatusCobranca
from core.models.fila_cobranca import FilaCobranca

# implementa a funcionalidade de acesso a dados da fila de cobrança
class FilaCobrancaService(FilaCobrancaInterface):

    def __init__(self, fila: FilaCobranca) -> None:
        self.fila = fila

    def incluir(self, cobranca: Cobranca) -> None:
        if cobranca.status != "PAGA" :
            self.fila.add_cobranca(cobranca)
            return True
    
    def processar_cobrancas(self) -> list: 

        cobrancas_pagas = []

        for cobranca in self.fila.get_all_conbrancas():
                try:
                    #aqui chama metodo que realiza cobranca (ainda vou implementar)
                    self.fila.retira_cobranca()
                    cobranca.set_status(StatusCobranca.PAGA.name)
                    cobrancas_pagas.append(cobranca)

                except:
                    cobranca.set_status(StatusCobranca.FALHA.name)
                    self.fila.add_cobranca(cobranca)
                    
        return cobrancas_pagas



#posso fazer outra manipulacoes de dados aqui 