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
