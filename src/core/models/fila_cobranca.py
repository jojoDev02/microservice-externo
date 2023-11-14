from queue import Queue
from core.models.cobranca import Cobranca

class FilaCobranca:
    
    def __init__(self) -> None:
        self.fila = Queue()

    def get_cobranca(self, cobranca_id: int) -> Cobranca:
        for cobranca in self.fila.queue:
            if cobranca.id == cobranca_id:
                return cobranca 
        return None

    def add_cobranca(self, cobranca: Cobranca) -> None:
        self.fila.put(cobranca)
        self._get_fila()
        

    def retira_cobranca(self) -> Cobranca:
       return self.fila.get()
    
    #apagar depois
    def _get_fila(self):
        for cobranca in self.fila.queue:
            print(cobranca.to_dict())
