# API 1º Semestre ADS

# Documentação - Sprint 2

<p align="center">
      <img src="../../img/logo-PigeonCode.png" alt="logo da equipe Pigeon Code" width="200">
      <h2 align="center"> Pigeon Code </h2>
</p>

<p align="center">
  | <a href ="#backlog-sprint"> Backlog da Sprint</a>  |   
  <a href ="#dor"> DoR</a> |
  <a href ="#dod"> DoD</a> |
  <a href ="#colaboradores"> Colaboradores</a> |
</p>
<br>

## 📋 Backlog da Sprint <a id="backlog-sprint"></a>

| Rank | Prioridade | Funcionalidade                                                      | Descrição                                                                                                                                                                                 | Estimativa | Sprint | Status |
| :--: | :--------: | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------: | :----: | :----: |
|  1   |    Alta    | Definir lógica de pontuação.                                        | Decidir os critérios de pontuação e peso das respostas para os formulários da área de treinamento. (Meta)                                                                                 |            |   2    |        |
|  2   |    Alta    | Prática do Flask-WTF.                                               | Praticar a criação e gerenciamento de formulários com o uso da biblioteca Flask-WTF e WTForms, a fim de replicar a lógica aos componentes do site. (Meta)                                 |            |   2    |        |
|  3   |   Média    | Estudar Formulários no Bootstrap.                                   | Praticar por meio de projetos rápidos e práticos e reunir conhecimentos suficientes para incluir formulários personalizados e estilizados no site. (Meta)                                 |            |   2    |        |
|  4   |    Alta    | Estrutura de BD para projetos e respostas.                          | Criar tabelas de projetos e respostas com seus respectivos relacionamentos no SQLite, seguindo o modelo definido. (Meta)                                                                  |            |   2    |        |
|  5   |   Média    | Elaborar as perguntas que serão feitas nos formulários avaliativos. | Reunir perguntas para os formulários com base no modo de pontuação definido pelo sistema avaliativo. (Meta)                                                                               |            |   2    |        |
|  6   |    Alta    | Funcionalidade de Submit de Formulários.                            | Desenvolver a lógica de envio dos formulários para que eles sejam armazenado no banco de dados efetivamente. Devem conter um campo para selecionar a qual projeto eles se referem. (Meta) |            |   2    |        |
|  7   |   Média    | Tratamento de erros formulários avaliativos.                        | Exibir mensagens de erro de validação para campos que forem obrigatórios nos formulários avaliativos. (Meta)                                                                              |            |   2    |        |
|  8   |   Média    | Tratamento de erros formulário de login.                            | Implementar a exibição das mensagens de erro de validação para os campos do formulário de login para o acesso ao administrador. (Meta)                                                    |            |   2    |        |
|  9   |   Média    | Funcionalidade de Logout de administrador.                          | Criar um botão com a lógica de logout, visível apenas na área de acesso restrito ao administrador e quando ele já estiver logado. (Meta)                                                  |            |   2    |        |
|  10  |   Média    | Funcionalidade de criar projetos na área de administrador.          | Criar um botão para criação dos projetos do administrador. Deve pedir apenas por nome e descrição.                                                                                        |            |   2    |        |
|  11  |   Baixa    | Refatoração de código da sidebar de navegação.                      | Refatorar o código da barra de navegação da área de treinamentos para utilizá-lo dentro da área de acesso restrito.                                                                       |            |   2    |        |
|  12  |   Baixa    | Filtrar as respostas dos formulários para suas respectivas sessões. | Cada resposta obtida nos formulários enviados deve ser mostrada no projeto em específico para o qual ele foi preenchido.                                                                  |            |   2    |        |
|  13  |   Baixa    | Incremento e Sprint Review.                                         | Gravar vídeo do incremento e preparar apresentação para o Sprint Review. (Meta)                                                                                                           |            |   2    |        |

<br>

## 📝 DoR - Definition of Ready <a id="dor"></a>

| Critério                         | Descrição                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| Clareza na descrição             | A User Story está escrita com títulos e descrições claras.                                 |
| Critérios de aceitação definidos | A história apresenta objetivos que indicam o que é necessário para considerá-la concluída. |
| Estimativas definidas            | A história foi pontuada e tem uma estimativa clara.                                        |

<br>

## 🏆 DoD - Definition of Done <a id="dod"></a>

| Critério                | Descrição                                                       |
| ----------------------- | --------------------------------------------------------------- |
| Código revisado         | Código revisado por pelo menos um colega da equipe.             |
| Telas funcionais        | Telas implementadas e funcionando.                              |
| Documentação atualizada | README ou documentação da sprint atualizadas com as alterações. |
| Vídeo Demo publicado    | Demonstração do Incremento da Sprint gravada e publicada.       |

<br>

## 🎓 Colaboradores <a id="colaboradores"></a>

<div align="center">
  <table>
    <tr>
      <th>Membro</th>
      <th>Função</th>
      <th>Github</th>
      <th>Linkedin</th>
    </tr>
    <tr>
      <td>Manuela Santos</td>
      <td>Scrum Master</td>
      <td><a href="https://github.com/manuoops"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/manuela-santos-098797351/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
      <td>Taís Souza</td>
      <td>Product Owner</td>
      <td><a href="https://github.com/tat4Souza"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/tais-f-souza"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
      <td>Adler Rocha</td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/AdlerR101"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/adler-rocha-a98480216"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
      <td>Daniel Nathan</td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/Danithan"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/daniel-leite-28220b384/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
     <tr>
      <td>Giovana Machado</td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/giovana777"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/giovana-machado-49b017384/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
     <tr>
      <td>Matheus Borges</td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/MGBorgess"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/matheus-de-oliveira-b68bbb383"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
    <td>Nicolas Pacheco</td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/Nocholas0"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/nicolas-santos-pacheco-591216287/?utm_source=share&utm_campaign=sha…"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
      <td>Vitor Bomfim </td>
      <td>Desenvolvedor</td>
      <td><a href="https://github.com/VitorBomfim-12"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a></td>
      <td><a href="https://www.linkedin.com/in/vitor-bomfim-122339289/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></td>
    </tr>
    <tr>
  </table>
</div>
