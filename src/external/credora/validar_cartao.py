import random
from core.interfaces.validar_cartao import CartaoValidatorInterface
from core.models.cartao_credito import CartaoCredito

class CartaoValidator(CartaoValidatorInterface):

# Este método simula a validação do cartão junto à credora.
    def validar(self, cartao):
        # fazer resquest para a credora passando os dados do cartao
        # processar resposta e retornar para o use_case
        return random.choice([True, False])