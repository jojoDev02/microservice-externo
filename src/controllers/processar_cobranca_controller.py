from core.use_cases.processar_cobrancas import ProcessarCobrancasUseCase


class ProcessarCobrancasController:

    def __init__(self, use_case: ProcessarCobrancasUseCase) -> None:
        self.__use_case = use_case

    def processar_cobrancas(self):

            cobrancas_pagas = self.__use_case.execute()


            return [cobranca.to_dict() for cobranca in cobrancas_pagas], 200
        
