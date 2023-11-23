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
        self.hora_solicitacao = str(datetime.datetime.now())
        self.hora_finalizacao = None
        self.valor = valor 
        self.ciclista = ciclista

   
    def __set_horario_finalizacao(self):
        self.hora_finalizacao = str(datetime.datetime.now())
   
    def __set_status(self, novo_status: StatusCobranca):
        self.status = novo_status
    
    def marcar_como_paga(self): 
        self.__set_status(StatusCobranca.PAGA.name)
        self.__set_horario_finalizacao()
    
    
    def marcar_como_falha(self): 
        self.__set_status(StatusCobranca.FALHA.name)
        self.__set_horario_finalizacao()

    def marcar_como_incluida(self):
        self.__set_horario_finalizacao()
        

    def get_status(self):
        return self.status

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'horaSolicitacao': self.hora_solicitacao,
            'horaFinalizacao': self.hora_finalizacao,
            'valor': self.valor,
            'ciclista': self.ciclista
        }