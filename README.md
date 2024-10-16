Sistema bancário simples feito em python, com as seguintes classes e relacionamentos:

Cliente: Representa um cliente do banco, com atributos como nome, CPF, endereço e uma lista de contas.
PessoaFisica: Herda de Cliente e adiciona atributos específicos para pessoas físicas, como CPF e data de nascimento.
Conta: Representa uma conta bancária, com atributos como saldo, número, agência e cliente.
ContaCorrente: Herda de Conta e adiciona atributos específicos para contas correntes, como limite e limite de saques.
Transacao: Representa uma transação bancária, com um método para registrar a transação em uma conta.
Historico: Armazena o histórico de transações de uma conta.
