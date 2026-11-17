# **Documento de Casos de Uso**

PROJETO · NEP – NÚCLEO DE ESTUDOS POLÍTICOS

**Versão:** 1.0

## **1\. Identificação dos atores**

| Ator | Descrição |
| ----- | ----- |
| **Visitante** | Pessoa que acessa o NEP sem possuir cadastro ou realizar login. |
| **Aluno** | Pessoa que solicitou inscrição, foi aprovada pelo administrador e possui acesso às funcionalidades destinadas aos estudantes. |
| **Professor** | Pessoa que solicitou inscrição, foi aprovada pelo administrador e possui acesso às funcionalidades de gerenciamento de materiais, resumos e acompanhamento dos alunos. |
| **Administrador** | Responsável pelo gerenciamento das inscrições, usuários, materiais e informações administrativas do NEP. |

## **2\. Casos de uso**

### **2.1. Visitante**

O visitante possui acesso limitado às informações públicas do NEP, sem necessidade de autenticação. Também pode solicitar inscrição como aluno ou professor.

| Código | Caso de uso | Descrição |
| ----- | ----- | ----- |
| UC01 | Consultar datas de inscrição | Visualizar os períodos e prazos de inscrição do NEP. |
| UC02 | Consultar resumos das aulas | Acessar os resumos das aulas publicados pelos professores. |
| UC03 | Consultar informações sobre o projeto | Visualizar os objetivos, a equipe responsável, a proposta e outras informações sobre o NEP. |
| UC04 | Solicitar inscrição como aluno | Preencher e enviar uma solicitação de inscrição como aluno. |
| UC05 | Solicitar inscrição como professor | Preencher e enviar uma solicitação de inscrição como professor. |

### **2.2. Aluno**

O aluno precisa ter sua inscrição aprovada pelo administrador e realizar login para acessar sua conta.

| Código | Caso de uso | Descrição |
| ----- | ----- | ----- |
| UC06 | Realizar login | Acessar sua conta utilizando e-mail e senha. |
| UC07 | Consultar materiais | Visualizar os materiais de estudo disponíveis. |
| UC08 | Consultar fontes | Visualizar as referências utilizadas nos materiais de estudo. |
| UC09 | Consultar resumos das aulas | Acessar os resumos publicados pelos professores. |
| UC10 | Consultar disciplinas e assuntos | Visualizar as disciplinas e os conteúdos abordados no curso. |
| UC11 | Consultar progresso | Acompanhar os conteúdos já concluídos e o andamento no curso. |
| UC12 | Encerrar sessão | Sair da conta. |

### **2.3. Professor**

O professor precisa ter sua inscrição aprovada pelo administrador e realizar login para acessar suas funcionalidades.

| Código | Caso de uso | Descrição |
| ----- | ----- | ----- |
| UC13 | Realizar login | Acessar sua conta utilizando e-mail e senha. |
| UC14 | Cadastrar material | Adicionar materiais de estudo à sua disciplina. |
| UC15 | Editar material | Alterar os próprios materiais cadastrados. |
| UC16 | Excluir material | Remover os próprios materiais cadastrados. |
| UC17 | Cadastrar fonte | Registrar fontes utilizadas nos materiais de estudo. |
| UC18 | Associar fonte ao material | Vincular fontes de referência aos respectivos materiais. |
| UC19 | Cadastrar resumo de aula | Registrar resumos das aulas ministradas. |
| UC20 | Editar resumo | Alterar os próprios resumos cadastrados. |
| UC21 | Excluir resumo | Remover os próprios resumos cadastrados. |
| UC22 | Visualizar conteúdos dos alunos | Consultar os conteúdos estudados pelos alunos. |
| UC23 | Confirmar conclusão de conteúdo | Confirmar que determinado aluno concluiu um conteúdo. |
| UC24 | Encerrar sessão | Sair da conta. |

### **2.4. Administrador**

O administrador possui acesso às funcionalidades administrativas do NEP.

| Código | Caso de uso | Descrição |
| ----- | ----- | ----- |
| UC25 | Realizar login | Acessar a área administrativa utilizando e-mail e senha. |
| UC26 | Consultar solicitações de inscrição | Visualizar as solicitações pendentes de alunos e professores. |
| UC27 | Aprovar inscrição de aluno | Autorizar a entrada de um aluno no NEP e liberar sua conta. |
| UC28 | Rejeitar inscrição de aluno | Recusar uma solicitação de inscrição de aluno. |
| UC29 | Aprovar inscrição de professor | Autorizar a entrada de um professor no NEP e liberar sua conta. |
| UC30 | Rejeitar inscrição de professor | Recusar uma solicitação de inscrição de professor. |
| UC31 | Visualizar usuários | Consultar os alunos e professores cadastrados no NEP. |
| UC32 | Gerenciar usuários | Administrar os cadastros existentes. |
| UC33 | Consultar materiais | Visualizar todos os materiais cadastrados. |
| UC34 | Gerenciar materiais | Editar ou excluir materiais cadastrados no NEP. |
| UC35 | Gerenciar informações do projeto | Administrar as datas de inscrição e as informações públicas do NEP. |
| UC36 | Encerrar sessão | Sair da conta administrativa. |

## **3\. Relacionamentos entre os casos de uso**

Algumas funcionalidades dependem de outras para serem executadas.

| Caso de uso | Relacionamento | Caso de uso relacionado |
| ----- | ----- | ----- |
| Cadastrar material | `<<include>>` | Associar fonte ao material |
| Realizar login | `<<include>>` | Verificar credenciais |
| Aprovar inscrição de aluno | `<<include>>` | Atualizar situação da inscrição |
| Aprovar inscrição de professor | `<<include>>` | Atualizar situação da inscrição |
| Confirmar conclusão de conteúdo | `<<include>>` | Atualizar progresso do aluno |

Esses relacionamentos representam etapas necessárias para a execução de determinadas funcionalidades.

## **4\. Regras de acesso dos atores**

| Funcionalidade | Visitante | Aluno | Professor | Administrador |
| ----- | ----- | ----- | ----- | ----- |
| Consultar datas de inscrição | Sim | Sim | Sim | Sim |
| Consultar informações do projeto | Sim | Sim | Sim | Sim |
| Consultar resumos das aulas | Sim | Sim | Sim | Sim |
| Solicitar inscrição como aluno | Sim | Não | Não | Não |
| Solicitar inscrição como professor | Sim | Não | Não | Não |
| Consultar materiais | Não | Sim | Sim | Sim |
| Consultar fontes | Não | Sim | Sim | Sim |
| Cadastrar materiais | Não | Não | Sim | Sim |
| Cadastrar resumos | Não | Não | Sim | Sim |
| Confirmar conclusão de conteúdo | Não | Não | Sim | Não |
| Consultar progresso dos alunos | Não | Não | Sim | Sim |
| Gerenciar usuários | Não | Não | Não | Sim |
| Gerenciar materiais | Não | Não | Próprios | Todos |
| Gerenciar informações do projeto | Não | Não | Não | Sim |

## **5\. Fluxo de inscrição**

O processo de inscrição será o mesmo para alunos e professores, mudando apenas a categoria selecionada.

## **Fluxo de inscrição no NEP**

1. **Acesso do visitante**  
   A pessoa acessa as informações públicas do NEP.  
2. **Escolha da inscrição**  
   Seleciona se deseja participar como aluno ou professor.  
3. **Preenchimento dos dados**  
   Informa nome, e-mail e senha.  
4. **Envio da solicitação**  
   O sistema registra a solicitação como pendente.  
5. **Análise do administrador**  
   O administrador consulta os dados e decide se aprova ou rejeita.  
6. **Resultado da inscrição**  
   Se aprovada, a conta é liberada. Se rejeitada, o acesso não é concedido.  
7. **Acesso à conta**  
   O usuário aprovado pode realizar login com seu e-mail e senha.

## **6\. Observações e decisões do projeto**

1\. **Inscrição de alunos e professores:** qualquer visitante poderá solicitar inscrição em uma das duas categorias.

2\. **Aprovação:** todas as solicitações dependerão da aprovação do administrador.

3\. **Identificação:** o e-mail será utilizado como login, acompanhado da senha individual.

4\. **Nome:** o nome será utilizado para identificação pessoal, não como credencial de acesso.

5\. **Materiais:** os professores poderão gerenciar apenas os próprios materiais, enquanto o administrador poderá gerenciar todos.

6\. **Fontes:** todos os materiais deverão possuir pelo menos uma fonte de referência.

7\. **Resumos:** serão disponibilizados publicamente, sem necessidade de login.

8\. **Progresso:** somente o professor responsável poderá confirmar a conclusão dos conteúdos estudados pelos alunos.

9\. **Acesso público:** visitantes terão acesso somente às datas de inscrição, aos resumos das aulas e às informações sobre o projeto.