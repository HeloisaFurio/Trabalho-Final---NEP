from classes import *
import os
import dados

from classes import Aluno
import dados

def cadastroAluno():
    limpar_tela()
    print("===== CADASTRO DE ALUNO =====")

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    for aluno in dados.alunos:
        if aluno.email == email:
            print("Já existe um aluno cadastrado com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    for cadastro in dados.cadastrosPendentes:
        if cadastro.email == email:
            print("Já existe uma solicitação com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    novo_aluno = Aluno(0, nome, email, senha)

    dados.cadastrosPendentes.append(novo_aluno)

    print("\nSolicitação de cadastro enviada!")
    print("Aguarde a aprovação de um administrador.")

helo = Administrador("Heloisa Furio Castilho", "heloisa.fc14@aluno.ifsc.edu.br", "1410")
juh = Administrador("Julia Zulian Lima", "julia.zl2010@aluno.ifsc.edu.br", "2201")

dados.administradores.append(helo)
dados.administradores.append(juh)

vagasAlunos = 40

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
4 - Consultar conteúdos
====================================
ACESSO:

5 - Cadastro de aluno
6 - Cadastro de professor
7 - Cadastro de administrador
8 - Login

0 - Sair
===================================="""

opcao_escolhida = -1
while opcao_escolhida != 0:
    limpar_tela()
    print(menuInicial)

    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        limpar_tela()
        print("""O projeto é um curso local, gratuito e anual
de formação política, voltado principalmente para
jovens, com aulas semanais e apoio de uma plataforma
online própria. Com foco na pluralidade de ideias, transparência
e fontes confiáveis, a iniciativa busca desenvolver o pensamento crítico
sem defender uma ideologia específica, preparando os alunos para
uma participação cidadã mais consciente.""")
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 2:
        limpar_tela()
        print("Equipe responsável pelo projeto:\n")
        for admin in dados.administradores:
            print(admin.listarADM())
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 3:
        limpar_tela()
        print(f"O número de vagas para alunos no NEP(Núcleo de Estudos Políticos) é de {vagasAlunos} vagas")
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 4:
        limpar_tela()

        print("===== RESUMOS DAS AULAS =====")

        if len(dados.resumos) == 0:
            print("Nenhum resumo cadastrado.")

        else:
            for resumo in dados.resumos:
                print(resumo.listarResumo())
                print("-----------------------------")
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 5:
        cadastroAluno()
        input("\nPressione ENTER para voltar...")