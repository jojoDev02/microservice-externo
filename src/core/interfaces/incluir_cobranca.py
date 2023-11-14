from abc import ABC, abstractmethod
from core.models.cobranca import Cobranca

class FilaCobrancaInterface(ABC):

    @abstractmethod
    def incluir(self, cobranca: Cobranca) -> None:
        pass
