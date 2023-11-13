from core.interfaces.validar_cartao import CartaoValidatorInterface
from core.models.cartaoCredito import CartaoCredito


class ValidarCartaoUseCase:

    def __init__(self, cartao_validator: CartaoValidatorInterface) -> None:
        self.cartao_validator = cartao_validator

    def execute(self, cartao: CartaoCredito):
        # Lógica fictícia para validar o cartão
        if (len(cartao.cvv) == 4):
            # Se a lógica de validação for bem-sucedida, use o cartão_validator para validações adicionais
            is_valido = self.cartao_validator.validar(cartao)

            return is_valido 
         


            
         
   
        
    
