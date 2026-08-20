def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("⚠️ Erro: Digite um número válido. Exemplo: 2000 ou 2000.50")

def obter_hora(mensagem):
    while True:
        try:
            hora = int(input(mensagem))

            if 0 <= hora <= 23:
                return hora
            else:
                print("⚠️ Erro: A hora deve estar entre 0 e 23.")

        except ValueError:
            print("⚠️ Erro: Digite um número inteiro válido.")

def obter_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in ["s", "n"]:
            return resposta

        print("⚠️ Erro: Responda apenas com 's' ou 'n'.")

def obter_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor >= 0:
                return valor
            else:
                print("⚠️ Erro: O valor não pode ser negativo.")

        except ValueError:
            print("⚠️ Erro: Digite um número inteiro válido.")

class Transacao:
    def __init__(self, valor, hora, novo_destinatario, transacoes_ultima_hora):
        self.valor = valor
        self.hora = hora
        self.novo_destinatario = novo_destinatario
        self.transacoes_ultima_hora = transacoes_ultima_hora

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

def mostrar_resultado(risco, classificacao, motivos):
    print()
    print(f"Risco: {risco}%")
    print(classificacao)

    print()
    print("Motivos: ")

    for motivo in motivos:
        print(f"- {motivo}")

def main():
    print("=== SISTEMA DE DETECÇÃO DE FRAUDES ===")

    valor = obter_float("Digite o valor da transferência: ")
    hora = obter_hora("Digite a hora da transferência: ")
    novo_destinatario = obter_sim_nao("Destinatário novo? (s/n): ")
    transacoes_ultima_hora = obter_inteiro_positivo("Quantas transações feitas na última hora?: ")

    nova_transacao = Transacao(valor, hora, novo_destinatario, transacoes_ultima_hora)

    detector = DetectorFraude()

    risco, motivos = detector.calcular_risco(nova_transacao)

    classificacao = detector.classificar_risco(risco)

    mostrar_resultado(
        risco,
        classificacao,
        motivos
    )

if __name__ == "__main__":
    main()