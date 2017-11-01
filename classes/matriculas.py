from alunos import Aluno
from disciplinas import Disciplina

class Matricula:

    def __init__(self):
        self.aluno = None
        self.disciplina = None
        self.data_matricula = None
        self.data_cancelamento = None
        self.data_confirmacao = None

    def altera_aluno(self, a):
        if type(a) == Aluno:
            self.aluno = a
            return True
        return False
    
    def altera_disciplina(self, disciplina):
        if type(disciplina) == Disciplina:
            self.disciplina = disciplina
            return True
        return False

    def retorna_disciplina(self):
        return self.disciplina

    def retorna_aluno(self):
        return self.aluno