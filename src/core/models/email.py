from uuid import uuid4


class Email:

    def __init__(self, destinatario: str, assunto: str, mensagem: str):
        self.id = uuid4()
        self.destinatario = destinatario
        self.assunto = assunto
        self.mensagem = mensagem

    def to_dict(self):
        return {
            'id': self.id,
            'destinatario': self.destinatario,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }