# é responsável por receber a entrada do usuário
# e chamar o serviço apropriado para processar essa entrada.

from core.models.cobranca import Cobranca
from core.use_cases.incluir_cobranca import IncluirCobrancaNaFilaUseCase


class CobrancaController:

    def __init__(self, use_case: IncluirCobrancaNaFilaUseCase) -> None:
        self.__use_case = use_case

   
    def incluir_cobranca(self, valor, ciclista):
        cobranca = Cobranca(valor, ciclista)
        resultado = self.__use_case.execute(cobranca)

        if resultado:
          return cobranca.to_dict(), 200
        else:
            return {
            "codigo" : "422",
            "mensagem" : "Dados Inválidos!"
            }, 422