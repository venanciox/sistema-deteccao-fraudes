from datetime import datetime
import csv
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

def exportar_relatorio(historico):
    if len(historico) == 0:
        return

    agora = datetime.now()

    data_hora_formatada = agora.strftime("%d-%m-%Y_%Hh%M")
    nome_arquivo = f"relatorio_fraudes_{data_hora_formatada}.csv"

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        colunas = ["valor_transferido", "risco_calculado", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)

        escritor.writeheader()

        for linha in historico:
            escritor.writerow(linha)

    print(f"Relatório exportado com sucesso: {nome_arquivo}")

def main():
    print("=== SISTEMA DE DETECÇÃO DE FRAUDES ===")

    detector = DetectorFraude()

    historico_analises = []

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Analisar nova transação")
        print("2. Ver histórico de análises")
        print("3. Sair")

        opcao = input("Escolha uma opção (1/2/3): ").strip()

        if opcao == "1":
            print("\n[ Nova Transação ]")
            valor = obter_float("Digite o valor da transferência: ")
            hora = obter_hora("Digite a hora da transferência: ")
            novo_destinatario = obter_sim_nao("Destinatário novo? (s/n): ")
            transacoes_ultima_hora = obter_inteiro_positivo("Quantas transações feitas na última hora?: ")
            
            nova_transacao = Transacao(valor, hora, novo_destinatario, transacoes_ultima_hora)
            risco, motivos = detector.calcular_risco(nova_transacao)
            classificacao = detector.classificar_risco(risco)

            mostrar_resultado(risco, classificacao, motivos)

            resultado = {
                "valor_transferido": valor,
                "risco_calculado": risco,
                "status": classificacao
            }

            historico_analises.append(resultado)

        elif opcao == "2":
            print("\n=== HISTÓRICO DE ANÁLISES ===")

            if len(historico_analises) == 0:
                print("Nenhuma transação foi analisada ainda.")
            else:
                contador = 1
                for analise in historico_analises:
                    v = analise["valor_transferido"]
                    r = analise["risco_calculado"]
                    s = analise["status"]

                    print(f"{contador}. Valor: R$ {v} | Risco: {r}% | {s}")
                    contador += 1

        elif opcao == "3":
            print("\nEncerrando o sistema. Até logo!")
            exportar_relatorio(historico_analises)
            break

        else:
            print("\nErro: Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()