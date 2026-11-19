
from classes import *
import os
import dados


##############################################################
# CADASTROS
##############################################################

def cadastroADM():
    limpar_tela()
    print("===== CADASTRO DE ADMINISTRADOR =====")

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    for admin in dados.administradores:
        if admin.email == email:
            print("Já existe um administrador com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    for cadastro in dados.cadastrosPendentes:
        if cadastro.email == email:
            print("Já existe uma solicitação com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    novo_admin = Administrador(nome, email, senha)

    dados.cadastrosPendentes.append(novo_admin)
    dados.salvarDados()

    print("\nSolicitação de cadastro enviada!")
    print("Aguarde a aprovação de um administrador.")


##############################################################

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
    dados.salvarDados()

    print("\nSolicitação de cadastro enviada!")
    print("Aguarde a aprovação de um administrador.")


##############################################################

def cadastroProfessor():
    limpar_tela()
    print("===== CADASTRO DE PROFESSOR =====")

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    formacao = input("Formação acadêmica: ")

    for professor in dados.professores:
        if professor.email == email:
            print("Já existe um professor cadastrado com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    for cadastro in dados.cadastrosPendentes:
        if cadastro.email == email:
            print("Já existe uma solicitação com esse e-mail!")
            input("\nPressione ENTER para voltar...")
            return

    novo_professor = Professor(0, nome, email, formacao, senha)

    dados.cadastrosPendentes.append(novo_professor)
    dados.salvarDados()

    print("\nSolicitação de cadastro enviada!")
    print("Aguarde a aprovação de um administrador.")


##############################################################
# MENU DO ADMINISTRADOR
##############################################################

def menuAdministrador(admin):
    opcao_escolhida = -1

    while opcao_escolhida != 0:
        limpar_tela()
        print(f"""=====================================
       ÁREA DO ADMINISTRADOR
=====================================

Bem-vindo(a), {admin.nome}!

1 - Gerenciar usuários
2 - Gerenciar materiais

0 - Sair
=====================================""")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            gerenciarUsuarios()

        elif opcao_escolhida == 2:
            gerenciarMateriais()

        elif opcao_escolhida == 0:
            print("Saindo da área administrativa...")

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def gerenciarUsuarios():
    opcao_escolhida = -1

    while opcao_escolhida != 0:
        limpar_tela()
        print("""=====================================
        GERENCIAR USUÁRIOS
=====================================

1 - Cadastros pendentes
2 - Consultar alunos
3 - Consultar professores
4 - Consultar administradores
5 - Remover usuário

0 - Voltar
=====================================""")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            consultarCadastros()

        elif opcao_escolhida == 2:
            consultarAlunos()

        elif opcao_escolhida == 3:
            consultarProfessores()

        elif opcao_escolhida == 4:
            consultarAdministradores()

        elif opcao_escolhida == 5:
            removerUsuario()

        elif opcao_escolhida != 0:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def consultarCadastros():
    while True:
        limpar_tela()
        print("===== CADASTROS PENDENTES =====")

        if len(dados.cadastrosPendentes) == 0:
            print("Não existem cadastros pendentes.")
            input("\nPressione ENTER para voltar...")
            return

        for i, cadastro in enumerate(dados.cadastrosPendentes):
            print(f"\nCadastro {i + 1}")
            print(f"Nome: {cadastro.nome}")
            print(f"E-mail: {cadastro.email}")

            if isinstance(cadastro, Aluno):
                print("Tipo: Aluno")

            elif isinstance(cadastro, Professor):
                print("Tipo: Professor")
                print(f"Formação: {cadastro.formacao}")

            elif isinstance(cadastro, Administrador):
                print("Tipo: Administrador")

            print("-----------------------------")

        print("\n1 - Selecionar cadastro")
        print("0 - Voltar")

        opcao_escolhida = input("\nEscolha uma opção: ")

        if opcao_escolhida == "1":
            try:
                numero = int(input("Número do cadastro: "))

                if 1 <= numero <= len(dados.cadastrosPendentes):
                    analisarCadastro(numero - 1)

                else:
                    print("Cadastro inválido!")
                    input("\nPressione ENTER para continuar...")

            except ValueError:
                print("Digite um número válido!")
                input("\nPressione ENTER para continuar...")

        elif opcao_escolhida == "0":
            return

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def analisarCadastro(indice):
    usuario = dados.cadastrosPendentes[indice]

    limpar_tela()
    print("===== ANALISAR CADASTRO =====")

    print(f"Nome: {usuario.nome}")
    print(f"E-mail: {usuario.email}")

    if isinstance(usuario, Aluno):
        print("Tipo: Aluno")

    elif isinstance(usuario, Professor):
        print("Tipo: Professor")
        print(f"Formação: {usuario.formacao}")

    elif isinstance(usuario, Administrador):
        print("Tipo: Administrador")

    print("\n1 - Aprovar cadastro")
    print("2 - Recusar cadastro")
    print("0 - Voltar")

    opcao_escolhida = input("\nEscolha uma opção: ")

    if opcao_escolhida == "1":

        if isinstance(usuario, Aluno):
            matriculas = [
                aluno.matricula for aluno in dados.alunos
            ]
            usuario.matricula = max(matriculas, default=0) + 1

            dados.alunos.append(usuario)
            dados.vagasAlunos -= 1

            if len(dados.turmas) > 0:
                dados.turmas[0].alunos.append(usuario)

        elif isinstance(usuario, Professor):
            matriculas = [
                professor.matricula
                for professor in dados.professores
            ]
            usuario.matricula = max(matriculas, default=0) + 1

            dados.professores.append(usuario)

            if len(dados.turmas) > 0:
                dados.turmas[0].professores.append(usuario)

        elif isinstance(usuario, Administrador):
            dados.administradores.append(usuario)

        dados.cadastrosPendentes.pop(indice)
        dados.salvarDados()

        print("\nCadastro aprovado!")

    elif opcao_escolhida == "2":
        dados.cadastrosPendentes.pop(indice)
        dados.salvarDados()

        print("\nCadastro recusado!")

    elif opcao_escolhida == "0":
        return

    else:
        print("\nOpção inválida!")

    input("\nPressione ENTER para continuar...")


##############################################################
# CONSULTAR USUÁRIOS
##############################################################

def consultarAlunos():
    limpar_tela()
    print("===== ALUNOS CADASTRADOS =====")

    if len(dados.alunos) == 0:
        print("\nNão existem alunos cadastrados.")

    else:
        for aluno in dados.alunos:
            print(aluno.listarAluno())
            print("-------------------------------------")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarProfessores():
    limpar_tela()
    print("===== PROFESSORES CADASTRADOS =====")

    if len(dados.professores) == 0:
        print("\nNão existem professores cadastrados.")

    else:
        for professor in dados.professores:
            print(professor.listarProf())
            print("-------------------------------------")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarAdministradores():
    limpar_tela()
    print("===== ADMINISTRADORES CADASTRADOS =====")

    if len(dados.administradores) == 0:
        print("\nNão existem administradores cadastrados.")

    else:
        for admin in dados.administradores:
            print(admin.listarADM())
            print("-------------------------------------")

    input("\nPressione ENTER para voltar...")


##############################################################
# REMOVER USUÁRIOS
##############################################################

def removerUsuario():
    while True:
        limpar_tela()
        print("""=====================================
          REMOVER USUÁRIO
=====================================

1 - Remover aluno
2 - Remover professor
3 - Remover administrador

0 - Voltar
=====================================""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = dados.alunos
            tipo = "aluno"

        elif opcao == "2":
            lista = dados.professores
            tipo = "professor"

        elif opcao == "3":
            lista = dados.administradores
            tipo = "administrador"

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        limpar_tela()
        print(f"===== REMOVER {tipo.upper()} =====")

        if len(lista) == 0:
            print(f"\nNão existem {tipo}s cadastrados.")
            input("\nPressione ENTER para continuar...")
            continue

        for i, usuario in enumerate(lista):
            print(f"\n{i + 1} - {usuario.nome} | {usuario.email}")

        try:
            numero = int(input("\nDigite o número do usuário: "))

            if numero < 1 or numero > len(lista):
                print("Número inválido!")
                input("\nPressione ENTER para continuar...")
                continue

            usuario = lista[numero - 1]

            print(f"\nUsuário selecionado: {usuario.nome}")
            confirmar = input(
                "Deseja realmente remover? (s/n): "
            ).lower()

            if confirmar == "s":
                lista.pop(numero - 1)

                if tipo == "aluno":
                    dados.vagasAlunos += 1

                    if len(dados.turmas) > 0:
                        dados.turmas[0].alunos = [
                            aluno
                            for aluno in dados.turmas[0].alunos
                            if aluno.email != usuario.email
                        ]

                elif tipo == "professor":
                    if len(dados.turmas) > 0:
                        dados.turmas[0].professores = [
                            professor
                            for professor in dados.turmas[0].professores
                            if professor.email != usuario.email
                        ]

                dados.salvarDados()
                print("\nUsuário removido com sucesso!")

            else:
                print("\nRemoção cancelada.")

        except ValueError:
            print("\nDigite um número válido!")

        input("\nPressione ENTER para continuar...")


##############################################################
# GERENCIAR MATERIAIS
##############################################################

def gerenciarMateriais():
    opcao_escolhida = -1

    while opcao_escolhida != 0:
        limpar_tela()
        print("""=====================================
        GERENCIAR MATERIAIS
=====================================

1 - Cadastrar aula
2 - Cadastrar conteúdo
3 - Cadastrar resumo
4 - Consultar materiais
5 - Remover material

0 - Voltar
=====================================""")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrarAula()

        elif opcao_escolhida == 2:
            cadastrarConteudo()

        elif opcao_escolhida == 3:
            cadastrarResumo()

        elif opcao_escolhida == 4:
            consultarMateriais()

        elif opcao_escolhida == 5:
            removerMaterial()

        elif opcao_escolhida != 0:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def cadastrarAula():
    limpar_tela()
    print("===== CADASTRAR AULA =====")

    titulo = input("Título da aula: ")
    materia = input("Matéria: ")
    data = input("Data da aula: ")

    conteudosAula = []

    while True:
        print("\n===== CONTEÚDOS DA AULA =====")

        if len(dados.conteudos) == 0:
            print("Não existem conteúdos cadastrados.")
            break

        for i, conteudo in enumerate(dados.conteudos):
            print(f"{i + 1} - {conteudo.titulo}")

        print("0 - Finalizar")

        try:
            opcao = int(input("\nEscolha um conteúdo para adicionar: "))

            if opcao == 0:
                break

            if 1 <= opcao <= len(dados.conteudos):
                conteudosAula.append(dados.conteudos[opcao - 1])
                print("Conteúdo adicionado!")

            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite um número válido!")

    nova_aula = Aula(titulo, materia, data, conteudosAula)

    dados.aulas.append(nova_aula)
    dados.salvarDados()

    print("\nAula cadastrada com sucesso!")
    input("\nPressione ENTER para voltar...")


##############################################################

def cadastrarConteudo():
    limpar_tela()
    print("===== CADASTRAR CONTEÚDO =====")

    titulo = input("Título do conteúdo: ")
    referencias = input("Referências: ")
    fonte = input("Fonte: ")

    novo_conteudo = Conteudo(titulo, referencias, fonte)

    dados.conteudos.append(novo_conteudo)
    dados.salvarDados()

    print("\nConteúdo cadastrado com sucesso!")
    input("\nPressione ENTER para voltar...")


##############################################################

def cadastrarResumo():
    limpar_tela()
    print("===== CADASTRAR RESUMO =====")

    titulo = input("Título do resumo: ")
    materia = input("Matéria: ")
    data = input("Data da aula: ")
    resumo = input("Resumo da aula: ")
    referencias = input("Referências: ")
    fonte = input("Fonte: ")

    if len(dados.professores) == 0:
        print("\nNão existem professores cadastrados.")
        input("\nPressione ENTER para voltar...")
        return

    print("\n===== PROFESSORES =====")

    for i, professor in enumerate(dados.professores):
        print(f"{i + 1} - {professor.nome}")

    try:
        opcao = int(input("\nSelecione o professor responsável: "))

        if opcao < 1 or opcao > len(dados.professores):
            print("Opção inválida!")
            input("\nPressione ENTER para voltar...")
            return

        professor = dados.professores[opcao - 1]

        novo_resumo = Resumo(
            titulo,
            materia,
            data,
            resumo,
            referencias,
            fonte,
            professor
        )

        dados.resumos.append(novo_resumo)
        dados.salvarDados()

        print("\nResumo cadastrado com sucesso!")

    except ValueError:
        print("\nDigite um número válido!")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarMateriais():
    while True:
        limpar_tela()
        print("""=====================================
        CONSULTAR MATERIAIS
=====================================

1 - Consultar aulas
2 - Consultar conteúdos
3 - Consultar resumos

0 - Voltar
=====================================""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("===== AULAS CADASTRADAS =====")

            if len(dados.aulas) == 0:
                print("\nNão existem aulas cadastradas.")

            else:
                for i, aula in enumerate(dados.aulas):
                    print(f"\nAula {i + 1}")
                    print(f"Título: {aula.titulo}")
                    print(f"Matéria: {aula.materia}")
                    print(f"Data: {aula.data}")

                    print("Conteúdos:")

                    if len(aula.conteudos) == 0:
                        print("Nenhum conteúdo associado.")

                    else:
                        for conteudo in aula.conteudos:
                            print(f"- {conteudo.titulo}")

                    print("-------------------------------------")

            input("\nPressione ENTER para voltar...")

        elif opcao == "2":
            limpar_tela()
            print("===== CONTEÚDOS CADASTRADOS =====")

            if len(dados.conteudos) == 0:
                print("\nNão existem conteúdos cadastrados.")

            else:
                for i, conteudo in enumerate(dados.conteudos):
                    print(f"\nConteúdo {i + 1}")
                    print(f"Título: {conteudo.titulo}")
                    print(f"Referências: {conteudo.referencias}")
                    print(f"Fonte: {conteudo.fonte}")
                    print("-------------------------------------")

            input("\nPressione ENTER para voltar...")

        elif opcao == "3":
            limpar_tela()
            print("===== RESUMOS CADASTRADOS =====")

            if len(dados.resumos) == 0:
                print("\nNão existem resumos cadastrados.")

            else:
                for resumo in dados.resumos:
                    print(resumo.listarResumo())
                    print("-------------------------------------")

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def removerMaterial():
    while True:
        limpar_tela()
        print("""=====================================
          REMOVER MATERIAL
=====================================

1 - Remover aula
2 - Remover conteúdo
3 - Remover resumo

0 - Voltar
=====================================""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = dados.aulas
            tipo = "aula"

        elif opcao == "2":
            lista = dados.conteudos
            tipo = "conteúdo"

        elif opcao == "3":
            lista = dados.resumos
            tipo = "resumo"

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        limpar_tela()
        print(f"===== REMOVER {tipo.upper()} =====")

        if len(lista) == 0:
            print(f"\nNão existem {tipo}s cadastrados.")
            input("\nPressione ENTER para continuar...")
            continue

        for i, material in enumerate(lista):
            print(f"\n{i + 1} - {material.titulo}")

        try:
            numero = int(input("\nDigite o número do material: "))

            if numero < 1 or numero > len(lista):
                print("Número inválido!")
                input("\nPressione ENTER para continuar...")
                continue

            material = lista[numero - 1]

            confirmar = input(
                f"\nDeseja realmente remover '{material.titulo}'? (s/n): "
            ).lower()

            if confirmar == "s":
                lista.pop(numero - 1)
                dados.salvarDados()
                print("\nMaterial removido com sucesso!")

            else:
                print("\nRemoção cancelada.")

        except ValueError:
            print("\nDigite um número válido!")

        input("\nPressione ENTER para continuar...")


##############################################################
# MENU DO ALUNO
##############################################################

def menuAluno(aluno):
    opcao_escolhida = -1

    while opcao_escolhida != 0:
        limpar_tela()
        print(f"""=====================================
             ÁREA DO ALUNO
=====================================

Bem-vindo(a), {aluno.nome}!

1 - Consultar aulas
2 - Consultar conteúdos
3 - Consultar turma
4 - Consultar meus dados

0 - Sair
=====================================""")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            consultarAulasAluno()

        elif opcao_escolhida == 2:
            consultarConteudosAluno()

        elif opcao_escolhida == 3:
            consultarTurmaAluno(aluno)

        elif opcao_escolhida == 4:
            consultarDadosAluno(aluno)

        elif opcao_escolhida == 0:
            print("Saindo da área do aluno...")

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def consultarAulasAluno():
    limpar_tela()
    print("===== AULAS DO NEP =====")

    if len(dados.aulas) == 0:
        print("\nNenhuma aula cadastrada.")

    else:
        for aula in dados.aulas:
            print(f"""
-------------------------------------
Título: {aula.titulo}
Matéria: {aula.materia}
Data: {aula.data}
-------------------------------------
Conteúdos:
""")

            if len(aula.conteudos) == 0:
                print("Nenhum conteúdo associado a esta aula.")

            else:
                for conteudo in aula.conteudos:
                    print(f"- {conteudo.titulo}")
                    print(f"  Referências: {conteudo.referencias}")
                    print(f"  Fonte: {conteudo.fonte}")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarConteudosAluno():
    limpar_tela()
    print("===== CONTEÚDOS DAS AULAS =====")

    if len(dados.conteudos) == 0:
        print("\nNenhum conteúdo cadastrado.")

    else:
        for conteudo in dados.conteudos:
            print(f"""
-------------------------------------
Título: {conteudo.titulo}
Referências: {conteudo.referencias}
Fonte: {conteudo.fonte}
-------------------------------------
""")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarDadosAluno(aluno):
    limpar_tela()
    print("===== MEUS DADOS =====")

    print(f"""
Nome: {aluno.nome}
Matrícula: {aluno.matricula}
E-mail: {aluno.email}
""")

    input("\nPressione ENTER para voltar...")


##############################################################

def consultarTurmaAluno(aluno):
    limpar_tela()
    print("===== MINHA TURMA =====")

    if len(dados.turmas) == 0:
        print("\nA turma ainda não foi cadastrada.")

    else:
        turma = dados.turmas[0]

        print(f"\nAno: {turma.ano}")

        print("\n===== ALUNOS =====")

        if len(turma.alunos) == 0:
            print("Nenhum aluno cadastrado na turma.")

        else:
            for colega in turma.alunos:
                print(colega.listarAluno())

        print("\n===== PROFESSORES =====")

        if len(turma.professores) == 0:
            print("Nenhum professor associado à turma.")

        else:
            for professor in turma.professores:
                print(professor.listarProf())

    input("\nPressione ENTER para voltar...")


##############################################################
# MENU DO PROFESSOR
##############################################################

def menuProfessor(professor):
    opcao_escolhida = -1

    while opcao_escolhida != 0:
        limpar_tela()
        print(f"""=====================================
             ÁREA DO PROFESSOR
=====================================

Bem-vindo(a), {professor.nome}!

1 - Cadastrar aula
2 - Cadastrar conteúdo
3 - Cadastrar resumo
4 - Consultar materiais
5 - Remover material
6 - Consultar turma

0 - Sair
=====================================""")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrarAula()

        elif opcao_escolhida == 2:
            cadastrarConteudo()

        elif opcao_escolhida == 3:
            cadastrarResumo()

        elif opcao_escolhida == 4:
            consultarMateriais()

        elif opcao_escolhida == 5:
            removerMaterial()

        elif opcao_escolhida == 6:
            consultarTurmaProfessor()

        elif opcao_escolhida == 0:
            print("Saindo da área do professor...")

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")


##############################################################

def consultarTurmaProfessor():
    limpar_tela()
    print("===== TURMA DO NEP =====")

    if len(dados.turmas) == 0:
        print("\nA turma ainda não foi cadastrada.")

    else:
        turma = dados.turmas[0]

        print(f"\nAno: {turma.ano}")

        print("\n===== ALUNOS =====")

        if len(turma.alunos) == 0:
            print("Nenhum aluno cadastrado na turma.")

        else:
            for aluno in turma.alunos:
                print(aluno.listarAluno())

        print("\n===== PROFESSORES =====")

        if len(turma.professores) == 0:
            print("Nenhum professor associado à turma.")

        else:
            for prof in turma.professores:
                print(prof.listarProf())

    input("\nPressione ENTER para voltar...")


##############################################################
# LOGIN
##############################################################

def login():
    limpar_tela()
    print("===== LOGIN NEP =====")

    email = input("E-mail: ")
    senha = input("Senha: ")

    for aluno in dados.alunos:
        if aluno.email == email and aluno.senha == senha:
            menuAluno(aluno)
            return

    for professor in dados.professores:
        if professor.email == email and professor.senha == senha:
            menuProfessor(professor)
            return

    for admin in dados.administradores:
        if admin.email == email and admin.senha == senha:
            menuAdministrador(admin)
            return

    print("\nE-mail ou senha incorretos!")
    input("\nPressione ENTER para voltar...")


##############################################################
# CONFIGURAÇÕES INICIAIS
##############################################################

# Criar administradores iniciais, caso não existam

if len(dados.administradores) == 0:

    helo = Administrador(
        "Heloisa Furio Castilho",
        "heloisa.fc14@aluno.ifsc.edu.br",
        "1410"
    )

    juh = Administrador(
        "Julia Zulian Lima",
        "julia.zl2010@aluno.ifsc.edu.br",
        "2201"
    )

    dados.administradores.append(helo)
    dados.administradores.append(juh)


##############################################################

# Criar a turma, caso não exista

if len(dados.turmas) == 0:
    turma = Turma(2026, [], [], dados.disciplinas)
    dados.turmas.append(turma)


##############################################################

# Remover alunos duplicados pelo e-mail

alunos_unicos = []

for aluno in dados.alunos:
    if not any(a.email == aluno.email for a in alunos_unicos):
        alunos_unicos.append(aluno)

dados.alunos[:] = alunos_unicos


##############################################################

# Remover professores duplicados pelo e-mail

professores_unicos = []

for professor in dados.professores:
    if not any(p.email == professor.email for p in professores_unicos):
        professores_unicos.append(professor)

dados.professores[:] = professores_unicos


##############################################################

# Corrigir matrículas dos alunos antigos

matricula = 1

for aluno in dados.alunos:
    if aluno.matricula <= 0:
        aluno.matricula = matricula

    matricula = max(matricula, aluno.matricula + 1)


##############################################################

# Corrigir matrículas dos professores antigos

matricula = 1

for professor in dados.professores:
    if professor.matricula <= 0:
        professor.matricula = matricula

    matricula = max(matricula, professor.matricula + 1)


##############################################################

# Atualizar os integrantes da turma

dados.turmas[0].alunos = dados.alunos.copy()
dados.turmas[0].professores = dados.professores.copy()


##############################################################
# LIMPAR TELA
##############################################################

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


##############################################################
# SALVAR DADOS
##############################################################

dados.salvarDados()


##############################################################
# MENU INICIAL
##############################################################

menuInicial = """=====================================
  NEP (Núcleo de Estudos Políticos)
=====================================

Olá! Seja bem-vindo ao nosso curso!

=====================================
INFORMAÇÕES:

1 - Sobre o curso
2 - Consultar equipe
3 - Consultar vagas
4 - Consultar conteúdos
=====================================
ACESSO:

5 - Cadastro de aluno
6 - Cadastro de professor
7 - Cadastro de administrador
8 - Login

0 - Sair
====================================="""

opcao_escolhida = -1

while opcao_escolhida != 0:
    limpar_tela()
    print(menuInicial)

    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        limpar_tela()
        print("""    O projeto é um curso local, gratuito e anual
    de formação política, voltado principalmente para
    jovens, com aulas semanais e apoio de uma plataforma
    online própria. Com foco na pluralidade de ideias,
    transparência e fontes confiáveis, a iniciativa busca
    desenvolver o pensamento crítico sem defender uma
    ideologia específica, preparando os alunos para uma
    participação cidadã mais consciente.""")

        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 2:
        limpar_tela()
        print("Equipe responsável pelo projeto:\n")

        for admin in dados.administradores:
            print(admin.listarADM())

        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 3:
        limpar_tela()
        print(
            f"O número de vagas disponíveis para alunos no "
            f"NEP (Núcleo de Estudos Políticos) é de "
            f"{dados.vagasAlunos} vagas"
        )

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

    elif opcao_escolhida == 6:
        cadastroProfessor()
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 7:
        cadastroADM()
        input("\nPressione ENTER para voltar...")

    elif opcao_escolhida == 8:
        login()

    elif opcao_escolhida == 0:
        print("Encerrando programa...")

    else:
        print("Opção inválida!")
        input("\nPressione ENTER para continuar...")
