from abc import ABC, abstractmethod
from core.models.cobranca import Cobranca

#verificar se é recebe um instancia de cobrança mermoS
class RealizarCobrancaInterface(ABC):

    @abstractmethod
    def efetuar(self, cobranca: Cobranca) -> None:
        pass
