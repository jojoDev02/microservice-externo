from flask import Blueprint, request
from core.controllers.enviar_email_controller import EnviarEmailController
from core.use_cases.enviar_email import EnviarEmailUseCase
from external.email.enviar_email import EmailService

email_bp = Blueprint('email', __name__)

email_service = EmailService()
enviar_email_usecase = EnviarEmailUseCase(email_service)
enviar_email_controller = EnviarEmailController(enviar_email_usecase)

@email_bp.route('/enviarEmail', methods=['POST'])
def enviar_email():
    data = request.get_json()
    destinatario = data['destinatario']
    assunto = data['assunto']
    mensagem= data['mensagem']

    # Chama o método do controller
    resultado, status_code = enviar_email_controller.enviar_email(destinatario, assunto, mensagem)

    return resultado, status_code

@email_bp.route('/', methods=['GET'])
def index():
    return 'WORKING'