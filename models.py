class Transacao:
    def __init__(self, valor, hora, novo_destinatario, transacoes_ultima_hora):
        self.valor = valor
        self.hora = hora
        self.novo_destinatario = novo_destinatario
        self.transacoes_ultima_hora = transacoes_ultima_hora