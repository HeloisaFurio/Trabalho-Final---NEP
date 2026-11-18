
import pickle
import os

ARQUIVO = "dados.pkl"

def carregarDados():
    dadosIniciais = {
        "alunos": [],
        "cadastrosPendentes": [],
        "professores": [],
        "administradores": [],
        "turmas": [],
        "disciplinas": [],
        "aulas": [],
        "conteudos": [],
        "resumos": [],
        "vagasAlunos": 40
    }

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "rb") as arquivo:
            dadosSalvos = pickle.load(arquivo)

        dadosIniciais.update(dadosSalvos)

    return dadosIniciais


dados = carregarDados()

alunos = dados["alunos"]
cadastrosPendentes = dados["cadastrosPendentes"]
professores = dados["professores"]
administradores = dados["administradores"]
turmas = dados["turmas"]
disciplinas = dados["disciplinas"]
aulas = dados["aulas"]
conteudos = dados["conteudos"]
resumos = dados["resumos"]
vagasAlunos = dados.get("vagasAlunos", 40)

def salvarDados():
    dados = {
        "alunos": alunos,
        "cadastrosPendentes": cadastrosPendentes,
        "professores": professores,
        "administradores": administradores,
        "turmas": turmas,
        "disciplinas": disciplinas,
        "aulas": aulas,
        "conteudos": conteudos,
        "resumos": resumos,
        "vagasAlunos": vagasAlunos
    }

    with open(ARQUIVO, "wb") as arquivo:
        pickle.dump(dados, arquivo)
