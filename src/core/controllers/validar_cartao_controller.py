
from core.models.cartaoCredito import CartaoCredito
from core.use_cases.validar_cartao import ValidarCartaoUseCase


class ValidarCartaoController:

    def __init__(self, use_case: ValidarCartaoUseCase) -> None: 
        self.__use_case = use_case

    def validar_cartao(self,nome_titular: str, numero: str, validade: str, cvv: str):
            
        cartao = CartaoCredito(nome_titular, numero, validade, cvv)
        resultado = self.__use_case.execute(cartao)

        if resultado:
            return {
                "codigo" : "200",
                "mensagem" : "Dados atualizados!"
            }, 200
        else:
            return {
                "codigo" : "422",
                "mensagem" : "Dados Inválidos!"
            }, 422