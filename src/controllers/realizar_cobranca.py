
from core.models.cobranca import Cobranca
from core.use_cases.realizar_cobranca import RealizarCobrancaUseCase


class RealizarCobrancaController:

    def __init__(self, use_case: RealizarCobrancaUseCase) -> None:
        self.__use_case = use_case

    def realizar_cobranca(self, valor, ciclista):
        cobranca = Cobranca(valor, ciclista)
        resultado = self.__use_case.execute(cobranca)

        if resultado:
          return cobranca.to_dict(), 200
        else:
            return {
            "codigo" : "422",
            "mensagem" : "Falha no processamento"
            }, 422
        