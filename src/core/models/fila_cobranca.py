from queue import Queue
from core.models.cobranca import Cobranca

class FilaCobranca:
    
    def __init__(self) -> None:
        self.fila = list()

    def get_cobranca(self, cobranca_id: str) -> Cobranca:
        for cobranca in self.fila:
            if cobranca.id == cobranca_id:
                return cobranca 
        return None

    def add_cobranca(self, cobranca: Cobranca) -> None:
        self.fila.append(cobranca)

    def retira_cobranca(self) -> Cobranca:
       return self.fila.pop(0)
    
    def get_all_conbrancas(self):
        return self.fila

