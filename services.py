class DetectorFraude:

    def calcular_risco(self, transacao):
        risco = 0
        motivos = []

        if transacao.valor > 4999:
            risco += 30
            motivos.append("Valor alto")

        if 0 <= transacao.hora <= 5:
            risco += 25
            motivos.append("Horário incomum")

        if transacao.novo_destinatario.lower() == "s":
            risco += 20
            motivos.append("Destinatário novo")

        if transacao.transacoes_ultima_hora >= 5:
            risco += 25
            motivos.append("Muitas transações recentes")

        risco = min(risco, 100)

        return risco, motivos

    def classificar_risco(self, risco):
        if risco >= 60:
            return "🔴 ALTO RISCO"
        elif risco >= 30:
            return "🟡 RISCO MÉDIO"
        else:
            return "🟢 BAIXO RISCO"
