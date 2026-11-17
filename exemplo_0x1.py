class Matricula:
    def __init__(self, numero, validade, cpf):
        self.numero = numero
        self.validade = validade
        self.cpf = cpf

class Aluno:
    def __init__(self, matricula: Matricula, nome: str, email: str,  senha: str):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha

    def listarAluno(self):
        return f"{self.matricula} | {self.nome} | {self.email}"

matricula_do_aluno1 = Matricula(12313123, "22/11/2030", "731273717")
aluno1 = Aluno(matricula_do_aluno1, "ignacio", "email@email", )






