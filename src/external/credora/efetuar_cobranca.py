import os
from core.interfaces.realizar_cobranca import ProcessadorCobrancaInterface
from core.models.cartao_credito import CartaoCredito
import stripe

from core.models.cobranca import Cobranca

class ProcessadorCobranca(ProcessadorCobrancaInterface):

    def efetuar(self, cobranca: Cobranca) -> bool:

        stripe.api_key = os.environ.get("KEY_STRIPE")

        try:
        
            stripe.PaymentIntent.create(
                amount=int(cobranca.valor),
                currency="brl",
                payment_method="pm_card_visa",
                )
            

            return True

        except stripe.error.CardError as e:
            return False, e.error.message

        



## falta criar a blueprint e testar
