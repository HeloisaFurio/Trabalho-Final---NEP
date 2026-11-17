from classes import *
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


menuInicial = """====================================
CURSO JOVEM
====================================

Olá! Seja bem-vindo ao nosso curso!

====================================
INFORMAÇÕES:

1 - Sobre o curso
2 - Consultar equipe
3 - Consultar vagas
4 - Consultar atividades
====================================
ACESSO:

5 - Cadastro de aluno
6 - Cadastro de professor
7 - Login

0 - Sair
===================================="""

opcao_escolhida = -1
while opcao_escolhida != 0:
    limpar_tela()
    print(menuInicial)

    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        limpar_tela()
        print("O projeto é um curso local, gratuito e anual de formação política, voltado principalmente para jovens, com aulas semanais e apoio de uma plataforma online própria. Com foco na pluralidade de ideias, transparência e fontes confiáveis, a iniciativa busca desenvolver o pensamento crítico sem defender uma ideologia específica, preparando os alunos para uma participação cidadã mais consciente.")
        input("Pressione ENTER para voltar...")
