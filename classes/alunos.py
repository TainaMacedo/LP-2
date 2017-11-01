from pessoas import Pessoa
from usuarios import Usuario

class Aluno(Pessoa, Usuario):

    def __init__(self):
        self.sigla_curso = ''
        self.matriculas = []

    def altera_sigla(self, sigla):
        if type(sigla) == str:
            self.sigla_curso = sigla
            return True
        return False

    def retorna_sigla(self):
        return self.sigla_curso

    