class Pessoa:

    def __init__(self):
        self.nome = ''
        self.celular = ''
        self.email = ''

    def altera_celular(self, celular):
        if type(celular) == str:
            self.celular = celular
            return True
        return False

    def retorna_celular(self):
        return self.celular

    def altera_email(self, email):
        if type(email) == str:
            self.email = email
            return True
        return False 

    def retorna_email(self):
        return self.email

    def altera_nome(self, nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False 

    def retorna_nome(self):
        return self.nome

