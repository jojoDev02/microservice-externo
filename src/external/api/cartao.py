from flask import Blueprint, request

from core.controllers.validar_cartao_controller import ValidarCartaoController
from core.use_cases.validar_cartao import ValidarCartaoUseCase
from external.credora.validar_cartao import CartaoValidator

cartao_bp = Blueprint('cartao', __name__)

cartao_validator = CartaoValidator()
validar_cartao_usecase = ValidarCartaoUseCase(cartao_validator)
validar_cartao_controller = ValidarCartaoController(validar_cartao_usecase)

@cartao_bp.route('/validaCartaoDeCredito', methods=['POST'])
def valida_cartao():
    data = request.get_json()

    nome_titular = data["nomeTitular"]
    numero = data["numero"]
    validade = data["validade"]
    cvv = data["cvv"]

    resultado, status_code = validar_cartao_controller.validar_cartao(nome_titular=nome_titular, numero=numero, validade=validade, cvv=cvv)

    return resultado, status_code