menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("FALHA NA OPERAÇÃO: Valor informado inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        limite_saques_excedido = numero_saques >= LIMITES_SAQUES

        if saldo_excedido:
            print("FALHA NA OPERAÇÃO: Saldo Insuficiente!")

        elif limite_excedido:
            print("FALHA NA OPERAÇÃO: Valor maior que o permitido por operação!")

        elif limite_saques_excedido:
            print("FALHA NA OPERAÇÃO: Número de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("FALHA NA OPERAÇÃO: Valor informado inválido!")

    elif opcao == "3":
        print("\n===============EXTRATO===============")
        print("Não há histórico de movimentação!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "0":
        break

    else:
        print("OPERAÇÃO INVÁLIDA. Digite novamente a operação desejada.")