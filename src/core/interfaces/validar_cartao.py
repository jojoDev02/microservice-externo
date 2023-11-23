from abc import ABC, abstractmethod

from core.models.cartao_credito import CartaoCredito

class CartaoValidatorInterface(ABC):
    @abstractmethod
    def validar(self, cartao: CartaoCredito):
        pass