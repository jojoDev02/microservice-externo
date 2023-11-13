from abc import ABC, abstractmethod

class CartaoValidatorInterface(ABC):
    @abstractmethod
    def validar(self, cartao):
        pass