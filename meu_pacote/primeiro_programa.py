class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.data_ultimo_saque = None 

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            return False

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif self.numero_saques >= 3:
            print("Você atingiu o limite máximo de saques diários.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 500:
            print("Valor do saque excede o limite diário.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("Saque realizado com sucesso!")

    def visualizar_extrato(self):
        print("=== Extrato ===")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")



conta = ContaBancaria()

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
        try:
            valor = float(input("Digite o valor a ser depositado: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")
        except ValueError:
            print("Valor inválido. Digite um número.")
    elif opcao == '2':
        try:
            valor = float(input("Digite o valor a ser sacado: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saque não realizado. Verifique as condições.")
        except ValueError:
            print("Valor inválido. Digite um número.")
    elif opcao == '3':
        conta.visualizar_extrato()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")