from core.interfaces.validar_cartao import CartaoValidatorInterface
from core.models.cartao_credito import CartaoCredito


class ValidarCartaoUseCase:

    def __init__(self, cartao_validator: CartaoValidatorInterface) -> None:
        self.cartao_validator = cartao_validator

    def execute(self, cartao: CartaoCredito):
            
            is_valido = self.cartao_validator.validar(cartao)

            return is_valido 
         


            
         
   
        
    
