def calcular_risco(valor, hora, novo_destinatario):
    risco = 0
    motivos = []

    if valor > 4999:
        risco += 30
        motivos.append("Valor alto")

    if 0 <= hora <= 5:
        risco += 25
        motivos.append("Horário incomum")

    if novo_destinatario.lower() == "s":
        risco += 20
        motivos.append("Destinatário novo")

    return risco, motivos

def classificar_risco(risco):
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

    valor = float(input("Digite o valor da transferência: "))
    hora = int(input("Digite a hora da transferência: "))
    novo_destinatario = input("Destinatário novo? (s/n): ")

    risco, motivos = calcular_risco(
        valor,
        hora,
        novo_destinatario
    )

    classificacao = classificar_risco(risco)

    mostrar_resultado(
        risco,
        classificacao,
        motivos
    )

if __name__ == "__main__":
    main()