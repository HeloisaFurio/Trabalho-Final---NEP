# **Documento de Requisitos do Sistema**

PROJETO · SISTEMA DE ESTUDOS POLÍTICOS

**Versão:** 1.3

## **1\. Requisitos funcionais (RF)**

Os requisitos funcionais descrevem as funcionalidades que o sistema deverá oferecer aos seus usuários.

### **1.1. Acesso aos conteúdos**

| Código | Descrição |
| ----- | ----- |
| RF01 | O sistema deve permitir que qualquer visitante consulte as informações gerais sem precisar realizar login. |
| RF02 | O sistema deve disponibilizar informações sobre o funcionamento do curso. |
| RF03 | O sistema deve permitir a consulta das disciplinas e dos assuntos abordados. |
| RF04 | O sistema deve permitir a consulta dos materiais de estudo cadastrados. |
| RF05 | O sistema deve permitir que os visitantes consultem as fontes utilizadas nos materiais. |

### **1.2. Cadastro de usuários**

| Código | Descrição |
| ----- | ----- |
| RF06 | O sistema deve permitir que visitantes solicitem inscrição como alunos.  |
| RF07 | O sistema deve permitir que visitantes solicitem inscrição como professores.  |
| RF08 | O sistema deve solicitar nome, e-mail e senha durante a inscrição . |
| RF09 | O sistema deve criptografar a senha |
| RF10  | O sistema deve gerar o login para o aluno |
| RF11 | O sistema deve gerar o login para o professor |
| RF12 | O sistema deve permitir que o administrador aprove ou rejeite as solicitações de inscrição de alunos e professores.  |
| RF13 | O sistema deve utilizar o e-mail do usuário como identificação para realizar o login.  |
| RF14 | O sistema deve armazenar os dados dos usuários cadastrados. |

### **1.3. Login e autenticação**

| Código | Descrição |
| ----- | ----- |
| RF15 | O sistema deve permitir que alunos realizem login utilizando login e senha. |
| RF16 | O sistema deve permitir que professores realizem login utilizando login e senha. |
| RF17 | O sistema deve permitir que administradores realizem login utilizando login e senha. |
| RF18 | O sistema deve verificar se o nome e a senha informados correspondem a um usuário cadastrado. |
| RF19 | O sistema deve identificar o tipo de usuário que realizou o acesso. |
| RF20 | O sistema deve permitir que o usuário encerre sua sessão. |
| RF21 | O sistema deve informar quando as credenciais de acesso forem inválidas. |

### **1.4. Gerenciamento de materiais**

| Código | Descrição |
| ----- | ----- |
| RF22 | O sistema deve permitir que professores cadastrem e publiquem materiais de estudo. |
| RF23 | O sistema deve permitir o cadastro de materiais nos formatos PDF, vídeos, artigos, textos e links externos. |
| RF24 | O sistema deve permitir o cadastro de materiais com título, descrição, disciplina e fonte de referência. |
| RF25 | O sistema deve permitir que professores editem os próprios materiais cadastrados. |
| RF26 | O sistema deve permitir que professores excluam os próprios materiais cadastrados. |
| RF27 | O sistema deve permitir que o administrador consulte e gerencie todos os materiais cadastrados. |
| RF28 | O sistema deve permitir a organização dos materiais por disciplina ou assunto. |

### **1.5. Gerenciamento de resumos das aulas**

| Código | Descrição |
| ----- | ----- |
| RF29 | O sistema deve permitir que professores cadastrem resumos das aulas referentes à sua disciplina. |
| RF30 | O sistema deve permitir o registro da data e do assunto de cada aula. |
| RF31 | O sistema deve permitir que professores editem e excluam os próprios resumos. |
| RF32 | O sistema deve disponibilizar os resumos cadastrados para consulta dos visitantes. |

### **1.6. Gerenciamento de fontes**

| Código | Descrição |
| ----- | ----- |
| RF33 | O sistema deve permitir o cadastro das fontes utilizadas nos materiais de estudo. |
| RF34 | O sistema deve permitir o registro do título, autor ou instituição responsável e link de acesso da fonte. |
| RF35 | O sistema deve permitir a associação das fontes aos respectivos materiais. |
| RF36 | O sistema deve permitir a consulta das fontes cadastradas. |

### **1.7. Acompanhamento dos alunos**

| Código | Descrição |
| ----- | ----- |
| RF37 | O sistema deve permitir que alunos consultem seu progresso no curso. |
| RF38 | O sistema deve permitir que professores visualizem os conteúdos estudados pelos alunos. |
| RF39 | O sistema deve permitir que professores confirmem a conclusão dos conteúdos pelos alunos. |
| RF40 | O sistema deve atualizar o progresso do aluno após a confirmação do professor. |

### **1.8. Gerenciamento de usuários**

| Código | Descrição |
| ----- | ----- |
| RF41 | O sistema deve permitir que o administrador visualize os usuários cadastrados. |
| RF42 | O sistema deve permitir que o administrador gerencie os cadastros de alunos e professores. |
|  |  |

## **2\. Requisitos não funcionais (RNF)**

Estabelecem critérios de segurança, confiabilidade e funcionamento do sistema.

| Código | Descrição |
| ----- | ----- |
| RNF01 | O sistema deve garantir o armazenamento dos dados cadastrados, mantendo as informações disponíveis após seu encerramento. |
| RNF02 | O sistema deve restringir o acesso às funcionalidades conforme o tipo de usuário. |
| RNF03 | O sistema deve proteger as informações pessoais dos usuários. |
| RNF04 | O sistema deve garantir o armazenamento seguro das senhas, impedindo que sejam visualizadas em sua forma original. |
| RNF05 | O sistema deve validar os dados informados durante os cadastros e acessos. |
| RNF06 | O sistema deve garantir a integridade das informações cadastradas. |
| RNF07 | O sistema deve permitir o acesso às informações públicas sem necessidade de autenticação. |

## **3\. Regras de negócio (RN)**

Definem as condições que devem ser respeitadas durante o funcionamento do sistema.

| Código | Descrição |
| ----- | ----- |
| RN01 | Os resumos das aulas devem estar disponíveis para consulta sem necessidade de login. |
| RN02 | Alunos, professores e administradores devem possuir diferentes níveis de acesso. |
| RN03 | Cada usuário deve possuir uma senha individual de acesso. |
| RN04 | Não será permitido o cadastro de usuários com e-mails já existentes.  |
| RN05 | As inscrições de professores dependerão da aprovação do administrador.  |
| RN06 | As inscrições de alunos dependerão da aprovação do administrador.  |
| RN07 | Os professores poderão cadastrar e publicar materiais sem aprovação prévia do administrador. |
| RN08 | Cada professor será responsável pelos materiais e resumos de sua disciplina. |
| RN09 | Todos os materiais cadastrados deverão possuir pelo menos uma fonte de referência. |
| RN10 | Os professores poderão gerenciar seus próprios materiais e resumos. |
| RN11 | O administrador poderá visualizar e gerenciar todos os materiais e usuários. |
| RN12 | Um conteúdo somente será considerado estudado após a confirmação do professor responsável. |
| RN13 | Os conteúdos deverão apresentar diferentes perspectivas políticas, respeitando a pluralidade de ideias. |
| RN14 | O cadastro de administradores será restrito a pessoas previamente autorizadas. |
| RN15 | O e-mail utilizado para identificação no sistema deverá ser exclusivo para cada usuário.  |
| RN16 | As solicitações de cadastro de alunos e professores deverão ser aprovadas pelo administrador antes que os usuários possam acessar suas contas.  |

