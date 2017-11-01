class Disciplina:

    def __init__(self):
        self.nome = ''
        self.carga_horaria = None 
        self.teoria = None  
        self.pratica = None 
        self.ementa = '' 
        self.competencias = '' 
        self.habilidades = '' 
        self.conteudo = ''
        self.bibliografia_basica = ''
        self.bibliografia_complementar = ''

    def altera_nome(self, nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False

    def retorna_nome(self):
        return self.nome
