print("=== SISTEMA DE DETECÇÃO DE FRAUDES ===")

valor = float(input("Digite o valor da transferência: "))
hora = int(input("Digite a hora da transferência: "))
novo_destinatario = input("Destinatário novo? (s/n): ")

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

print()
print(f"Risco: {risco}%")

if risco >= 60:
    print("🔴 ALTO RISCO")

elif risco >= 30:
    print("🟡 RISCO MÉDIO")

else:
    print("🟢 BAIXO RISCO")

print()
print("Motivos: ")

for motivo in motivos:
    print(f"- {motivo}")