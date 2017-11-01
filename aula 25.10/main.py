from clientes import Cliente
from contas import Conta
from bancos import Banco

c1 = Cliente('Ana', '123455678')
c2  = Cliente('Bernando', '98765432')

conta1 = Conta(100, [c1, c2], 123456)
conta2 = Conta(200, [c2], 23456)

banco = Banco('Banco FIT')
banco.abre_conta(conta1)
banco.abre_conta(conta2)

banco.lista_contas()
conta1.deposito(50)
banco.lista_contas()