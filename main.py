from validators import obter_float, obter_hora, obter_sim_nao, obter_inteiro_positivo
from models import Transacao
from services import DetectorFraude

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