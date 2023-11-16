# é responsável por receber a entrada do usuário
# e chamar o serviço apropriado para processar essa entrada.

from core.models.cobranca import Cobranca
from core.use_cases.obter_cobranca import ObterCobrancaUseCase


class ObterCobrancaController:

    def __init__(self, use_case: ObterCobrancaUseCase) -> None:
        self.__use_case = use_case

    
    def obter_cobranca(self, cobranca_id):
        cobranca = self.__use_case.execute(cobranca_id)

        if cobranca is not None:
          return cobranca.to_dict(), 200
        else:
            return {
            "codigo" : "404",
            "mensagem" : "Não encontrado."
            }, 404
        
 