from flask import Blueprint, request

from controllers.incluir_cobranca import IncluirCobrancaController
from controllers.obter_cobranca import ObterCobrancaController
from controllers.processar_cobranca_controller import ProcessarCobrancasController
from core.models.fila_cobranca import FilaCobranca
from core.services.cobranca_service import FilaCobrancaService
from core.use_cases.incluir_cobranca import IncluirCobrancaNaFilaUseCase
from core.use_cases.obter_cobranca import ObterCobrancaUseCase
from core.use_cases.processar_cobrancas import ProcessarCobrancasUseCase

cobranca_bp = Blueprint('cobranca', __name__)

fila = FilaCobranca()
fila_cobranca_service = FilaCobrancaService(fila) 

incluir_cobranca_usecase = IncluirCobrancaNaFilaUseCase(fila_cobranca_service)
cobranca_controller = IncluirCobrancaController(incluir_cobranca_usecase)


processa_cobrancas_usecase = ProcessarCobrancasUseCase(fila_cobranca_service)
processar_cobranca_controller = ProcessarCobrancasController(processa_cobrancas_usecase)

obter_cobranca_usecase = ObterCobrancaUseCase(fila_cobranca_service)
obter_cobranca_controller = ObterCobrancaController(obter_cobranca_usecase)

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

@cobranca_bp.route('/cobranca/<cobranca_id>', methods = ['GET'])
def get_cobranca(cobranca_id):

    resultado, status_code = obter_cobranca_controller.obter_cobranca(cobranca_id)
    
    return resultado, status_code

@cobranca_bp.route('/processaCobrancasEmFila', methods =['POST'])
def processa_cobrancas():

    resultado, status_code = processar_cobranca_controller.processar_cobrancas()

    
    return resultado, status_code