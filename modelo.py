# matricula, nome completo, nacimento, rg, cpf.
class Aluno():
    def __init__(self, matricula, nome, data_nascimento, rg, cpf):
        self.matricula = matricula
        self.nome = nome 
        self.data_nascimento = data_nascimento
        self.rg = rg 
        self.cpf = cpf
    
    def tete(self):
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'RG: {self.rg}')
        print(f'CPF: {self.cpf}')