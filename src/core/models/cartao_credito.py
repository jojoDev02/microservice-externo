class CartaoCredito:
    def __init__(self, nome_titular: str, numero: str, validade: str, cvv: str):
        self.nome_titular = nome_titular
        self.numero = numero
        self.validade = validade
        self.cvv = cvv

    
    #   responses:
    #     "200":
    #       description: Dados atualizados
    #     "422":
    #       description: Dados Inválidos