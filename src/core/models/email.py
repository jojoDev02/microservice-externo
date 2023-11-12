class Email:

    def __init__(self, destinatario: str, assunto: str, mensagem: str):
        self.destinatario = destinatario
        self.assunto = assunto
        self.mensagem = mensagem

    def to_dict(self):
        return {
            'destinatario': self.destinatario,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }