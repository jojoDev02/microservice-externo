import datetime
from uuid import uuid4
from enum import Enum, auto


class StatusCobranca(Enum):
    PENDENTE = 1
    PAGA = 2
    FALHA = 3
    CANCELADA = 4
    OCUPADA = 5



class Cobranca:
    
    def __init__(self, valor, ciclista) -> None:
        self.id = uuid4()
        self.status = StatusCobranca.PENDENTE.name
        self.horaSolicitacao = str(datetime.datetime.now())
        self.horaFinalizacao = None
        self.valor = valor 
        self.ciclista = ciclista

    def set_horario_finalizacao(self):
        self.horaFinalizacao = str(datetime.datetime.now())

    def set_status(self, novo_status: StatusCobranca):
        if novo_status not in StatusCobranca:
            raise ValueError("Status Inválido.")
        self.status = novo_status
    
    def get_status(self):
        return self.status

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'horaSolicitacao': self.horaSolicitacao,
            'horaFinalizacao': self.horaFinalizacao,
            'valor': self.valor,
            'ciclista': self.ciclista
        }