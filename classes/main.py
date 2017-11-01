from alunos import Aluno
from pessoas import Pessoa
from professores import Professor
from disciplinas import Disciplina
from matriculas import Matricula

aluno1 = Aluno()
aluno1.altera_celular('999999999')

celular_aluno = aluno1.retorna_celular()
print (celular_aluno)

professor1 = Professor()
professor1.nome = 'Fernando'

lp2 = Disciplina()
lp2.altera_nome('Linguagem de Programação 2')
professor1.adiciona_disciplina(lp2)

lp1 = Disciplina()
lp1.altera_nome('Linguagem de Programação 1')
professor1.adiciona_disciplina(lp1)

lista_disciplinas = professor1.disciplinas_professor()

for disciplina in lista_disciplinas: 
    print(disciplina.retorna_nome())

disciplina = Disciplina()
disciplina.altera_nome('Linguagem de Programação 1')
professor1.remove_disciplina(disciplina)
print(disciplina == lp1)

for disciplina in lista_disciplinas: 
    print(disciplina.retorna_nome())

matricula = Matricula()

matricula.altera_aluno(aluno1)
matricula.altera_disciplina(lp2)

disciplinaAluno = matricula.retorna_disciplina()
print("Disciplina aluno:", disciplinaAluno.retorna_nome())
