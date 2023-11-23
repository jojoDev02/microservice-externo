from core.interfaces.validar_cartao import CartaoValidatorInterface
from core.models.cartao_credito import CartaoCredito
import stripe

class CartaoValidator(CartaoValidatorInterface):

    def validar(self, cartao):
    
        # Definir as credenciais do Stripe
        stripe.api_key = "sk_test_51OF4VxHNHAeQ4rJ2Thenk7RXmKUsf8vj2F5DomvcT50Fzla7UNB37CorUMRG1QjlwnJZ8uN3I9o1kWexjlafZK9E00ROi0GFqg"

        try:

            token = stripe.Token.create(
                card={
                    'number': '4000056655665556',  # Número de teste da Stripe
                    'exp_month': '12',
                    'exp_year': '2024',
                    'cvc': '123'
                }
            )
            
            return True
        
        except stripe.error.CardError as e:
            return False, e.error.message

        