class Conta:

    def __init__(self, saldo, clientes, numero):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        if saldo > 0:
            self.deposito(saldo)

    def resumo(self):
        print('CC número: {}, Saldo: {}'
            .format(self.numero, self.saldo))

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.operacoes.append(('SAQUE', valor))

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(('DEPOSITO', valor))

    def extrato(self):
        for op in self.operacoes:
            print('{} --- {}'.format(op[0],op[1]))
        print('Saldo atual: ', self.saldo)
