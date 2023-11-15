from core.interfaces.fila_cobranca import FilaCobrancaInterface

class ProcessarCobrancasUseCase:

    def __init__(self, fila_cobranca: FilaCobrancaInterface) -> None:
        self.fila_cobranca = fila_cobranca

    def execute(self) -> list:

        processadas = self.fila_cobranca.processar_cobrancas()

        return processadas