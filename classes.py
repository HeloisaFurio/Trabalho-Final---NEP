from ast import List
class Visitante:
    def __init__(self, email: str):
        self.email = email

class Aluno:
    def __init__(self, matricula: int, nome: str, email: str,  senha: str):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha

    def listarAluno(self):
        return f"{self.matricula} | {self.nome} | {self.email}"


class Professor:
    def __init__(self, matricula: int, nome: str, email: str, formacao: str, senha:str):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.formacao = formacao
        self.senha = senha

    def listarProf(self):
        return f"{self.matricula} | {self.nome} | {self.email} | {self.formacao}"

class Administrador:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def listarADM(self):
        return f"{self.nome} | {self.email}"

class Turma:
    def __init__(self, ano: int, alunos, professores, disciplinas):
        self.ano = ano
        self.alunos = alunos
        self.professores = professores
        self.disciplinas = disciplinas

# turmas = []
# #vou crir a primeira turma

# professor1 = Professor(321, "Waltrik", "walwal@gmail.com", "graduacao", "senha123")

# turma_portuges2028 = Turma("2028", [], [professor1])
# turmas.append(turma_portuges2028)

# aluno1 = Aluno(123, "ignacio", "ignacio@email.com", "senha123")
# aluno2 = Aluno(123, "ryan", "ryan@email.com", "senha123")

# turmas[0].alunos.append(aluno1)


class Disciplina:
    def __init__(self, nome: str, sigla: str, cargaHoraria: int, aulas):
        self.nome = nome
        self.sigla = sigla
        self.cargaHoraria = cargaHoraria
        self.aulas = aulas

class Aula:
    def __init__(self, titulo: str, materia: str, data: int, conteudos):
        self.titulo = titulo
        self.materia = materia
        self.data = data
        self.conteudos = conteudos

class Conteudo:
    def __init__(self, titulo: str, referencias: str, fonte: str):
        self.titulo = titulo
        self.referencias = referencias
        self.fonte = fonte

class Resumo:
    def __init__(self, titulo: str, materia: str, data: str,
                 resumo: str, referencias: str, fonte: str, professor):

        self.titulo = titulo
        self.materia = materia
        self.data = data
        self.resumo = resumo
        self.referencias = referencias
        self.fonte = fonte
        self.professor = professor

    def listarResumo(self):
        return f"""
        Título: {self.titulo}
        Matéria: {self.materia}
        Data: {self.data}
        Resumo: {self.resumo}
        Referências: {self.referencias}
        Fonte: {self.fonte}
        Professor: {self.professor.nome}
        """