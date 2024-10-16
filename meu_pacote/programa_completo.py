from datetime import date

class PessoaFisica:
    def __init__(self, nome, cpf, endereco, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento

class Cliente(PessoaFisica):
    def __init__(self, nome, cpf, endereco, data_nascimento):
        super().__init__(nome, cpf, endereco, data_nascimento)
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Transacao:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo  

    def registrar(self, conta):
        if self.tipo == 'deposito':
            conta.depositar(self.valor)
        elif self.tipo == 'saque':
            conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def depositar(self, valor):
        self.saldo += valor
        transacao = Transacao(valor, 'deposito')
        self.historico.adicionar_transacao(transacao)
        return True

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            transacao = Transacao(valor, 'saque')
            self.historico.adicionar_transacao(transacao)
            return True
        else:
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques


cliente1 = Cliente("João da Silva", "12345678901", "Rua A, 123", date(1990, 1, 1))
conta_corrente = ContaCorrente(cliente1, 1234, "001", 1000, 3)
conta_corrente.depositar(500)
conta_corrente.sacar(200)