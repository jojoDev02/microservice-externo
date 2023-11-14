from flask import Blueprint, request

from core.controllers.incluir_cobranca import CobrancaController
from core.models.fila_cobranca import FilaCobranca
from core.services.cobranca_service import CobrancaService
from core.use_cases.incluir_cobranca import IncluirCobrancaNaFilaUseCase

cobranca_bp = Blueprint('cobranca', __name__)

fila = FilaCobranca()
fila_cobranca_service = CobrancaService(fila) 
incluir_cobranca_usecase = IncluirCobrancaNaFilaUseCase(fila_cobranca_service)
cobranca_controller = CobrancaController(incluir_cobranca_usecase)

@cobranca_bp.route('/cobranca', methods=['POST'])
def realizar_cobranca():
    return "ok"

@cobranca_bp.route('/filaCobranca',  methods=['POST'])
def incluir_cobranca():
    data = request.get_json()
    valor = data["valor"]
    ciclista = data["ciclista"]
    
    resultado, status_code = cobranca_controller.incluir_cobranca(valor, ciclista)

    return resultado, status_code

@cobranca_bp.route('/cobranca/<idCobranca>')
def get_cobranca(cobranca_id):
    pass

@cobranca_bp.route('/processaCobrancasEmFila')
def processa_cobrancas():
    pass