def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(valor):
    global saldo, extrato, numero_saques
    if numero_saques >= 3:
        print("Você atingiu o limite máximo de saques diários.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 500:
        print("Valor do saque excede o limite diário.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

def visualizar_extrato():
    global extrato, saldo
    print("=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")


saldo = 0
extrato = ""
numero_saques = 0

while True:
    print("=== Menu ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor a ser sacado: "))
        sacar(valor)
    elif opcao == '3':
        visualizar_extrato()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")