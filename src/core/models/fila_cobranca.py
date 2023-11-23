from collections import deque
from queue import Queue
import uuid
from core.models.cobranca import Cobranca

class FilaCobranca:
    
    def __init__(self) -> None:
        self.fila = deque()

    def get_cobranca(self, cobranca_id: str) -> Cobranca:
        cobranca_id = uuid.UUID(cobranca_id)
        for cobranca in self.fila:
            if cobranca.id == cobranca_id:
                return cobranca
        return None 

    def add_cobranca(self, cobranca: Cobranca) -> None:
        self.fila.append(cobranca)
        cobranca.marcar_como_incluida()


    def retira_cobranca(self) -> Cobranca:
        if self.fila:
            return self.fila.popleft()  # Utiliza popleft() para remover o primeiro elemento da fila
        else:
            return None  # Retorna None se a fila estiver vazia
        
    def get_all_cobrancas(self) -> Queue:
        return self.fila

