# matricula, nome completo, nacimento, rg, cpf.
class Aluno():
    Matriculas = 0
    
    def __init__(self, nome, data_nascimento, nacionalidade, cpf):
        
        Aluno.Matriculas =+ 1 
        
        self.nome = nome 
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade 
        self.cpf = cpf
        self.matricula = Aluno.Matriculas
        


    def Exibe_dados(self):
        
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'Nacionalidade: {self.nacionalidade}')
        print(f'CPF: {self.cpf}')