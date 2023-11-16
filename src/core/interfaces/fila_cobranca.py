from abc import ABC, abstractmethod
from core.models.cobranca import Cobranca

class FilaCobrancaInterface(ABC):

    @abstractmethod
    def incluir(self, cobranca: Cobranca) -> None: pass
    
    @abstractmethod
    def processar_cobrancas(self) -> list: pass

    @abstractmethod
    def obter_cobranca(self, cobranca_id) -> Cobranca: pass