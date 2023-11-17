import datetime
import random
from core.interfaces.validar_cartao import CartaoValidatorInterface
from core.models.cartao_credito import CartaoCredito


class CartaoValidator(CartaoValidatorInterface):

    # Este método simula a validação do cartão junto à credora.
    def validar(self, cartao):

        # validar o número do cartão
        if not self.validar_numero_cartao(cartao.numero_cartao):
            return False

        # validar o CVV
        if not self.validar_cvv(cartao.cvv):
            return False

        # validar a validade
        if not self.validar_validade(cartao.validade):
            return False

        return True

    # Método para validar o número do cartão
    def validar_numero_cartao(self, numero_cartao):
        # verificar se o número do cartão tem o tamanho correto
        if len(numero_cartao) != 16:
            return False

        # verificar se o número do cartão começa com um dígito correto
        if numero_cartao[0] not in ['4', '5', '6', '3']:
            return False

        # verificar se o número do cartão é válido usando o algoritmo de Luhn
        return self.validar_luhn(numero_cartao)

    # Método para validar o CVV
    def validar_cvv(self, cvv):
        # verificar se o CVV tem o tamanho correto
        if len(cvv) != 3:
            return False

        # verificar se o CVV é um número válido
        try:
            int(cvv)
            return True
        except ValueError:
            return False

    # Método para validar a validade
    def validar_validade(self, validade):
        # verificar se a validade tem o formato correto
        if len(validade) != 5:
            return False

        # verificar se o mês da validade é um número válido
        try:
            mes = int(validade[:2])
            if mes < 1 or mes > 12:
                return False
        except ValueError:
            return False

        # verificar se o ano da validade é um número válido
        try:
            ano = int(validade[3:])
            if ano < 100 or ano > 9999:
                return False
        except ValueError:
            return False

        # verificar se a validade está dentro do período de validade
        hoje = datetime.date.today()
        ano_atual = hoje.year
        if ano < ano_atual:
            return False
        if ano == ano_atual and mes < hoje.month:
            return False

        return True
