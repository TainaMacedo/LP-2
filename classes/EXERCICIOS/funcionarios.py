class Funcionario:

    def __init__(self, nome, salario):
        self.nome = ''
        self.salario = salario

    def aumentarSalario(self, aumento):
        self.salario = self.salario +(self.salario*(aumento/100))

    def retorna_salarioAtual(self):
        return self.salario
        

