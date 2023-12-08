from datetime import datetime
import re


class CartaoCredito:
    def __init__(self, nome_titular: str, numero: str, validade: str, cvv: str):
        self.nome_titular = nome_titular
        self.numero = numero
        self.validade = validade
        self.cvv = cvv


    def valida_formato(self):
        if (
            re.match(r"^\d{16}$", self.numero) is not None
            and self.__valida_validade()
            and re.match(r"^\d{3}$", self.cvv) is not None
        ):
            return True
        else:
            return False

    def __valida_validade(self):
        try:
            data_validade = datetime.strptime(self.validade, "%Y-%m-%d")
            return data_validade >= datetime.now()
        except ValueError:
            return False
    