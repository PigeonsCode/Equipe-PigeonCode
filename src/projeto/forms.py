from flask_wtf import FlaskForm #biblioteca que permite a criação de formulários de login
from wtforms import StringField, PasswordField,SubmitField,RadioField #importação dos campos dos formulários
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError #importação de funções que validam as informações inseridas 
#pelo usuário
from projeto.models import Adm_User



class FormLoginAdm(FlaskForm):
    username_adm = StringField("Nome de Usuário",validators=[DataRequired()])
    password_adm= PasswordField("Senha", validators=[DataRequired()])
    submit_button =  SubmitField("Entrar")
#validação dos dados inseridos pelo usuário

class FormUserAvalia(FlaskForm):
    # Inserir a numeração correta das perguntas e inserir coerce=int em todas as perguntas,
    #para que haja a conversão de string para int


     incremento_do_produto_p9 = RadioField("Como foi a satisfação do cliente em relação à entrega do incremento do produto ao final do Sprint?",
                          choices=[
                          (4,"O cliente está completamente satisfeito e ansioso para a próxima entrega. Foram feitas nulas ou poucas críticas a respeito do que lhe foi apresentado e o feedback se manteve positivo em praticamente toda sua extensão."),
                          (3,"Cliente satisfeito, porém aponta refinamentos. Foram feitas poucas críticas leves e quase nenhuma crítica extensa. O feedback foi majoritariamente positivo, poucas mudanças solicitadas."),
                          (2,"O cliente está insatisfeito e exigente para a próxima entrega. Foram feitas muitas críticas leves e muitas críticas extensas. O feedback pendeu mais para o lado negativo do que positivo e mudanças drásticas foram solicitadas."),
                          (1,"Cliente extremamente insatisfeito e risco de desistência. Foram feitas apenas críticas extensas. O feedback foi completamente negativo e a continuação do projeto está ameaçada.")],validators=[DataRequired()])
    
     inscremento_do_produto_p10 = RadioField("O incremento do produto atendeu a todas as tarefas definidas na versão final do Sprint Backlog?",
                          choices=[
                          (4,"Sim, todas as tarefas obrigatórias foram concluídas com êxito e também as definidas como metas complementares. O maior valor de produto para aquela Sprint foi entregue com sucesso."),
                          (3,"Parcialmente, todas as tarefas obrigatórias foram concluídas, porém algumas ou todas as complementares foram deixadas para a próxima Sprint. O valor do incremento do produto entregue foi alto."),
                          (2,"Minimamente, algumas tarefas obrigatórias não foram concluídas e nenhuma das complementares. O valor do produto entregue foi menor do que o prometido."),
                          (1,"Não, nenhuma tarefa foi concluída como o planejado e o valor do produto entregue não foi cumprido, ameaçando a completude das próximas Sprints.")],validators=[DataRequired()])


     incremento_do_produto_p11 = RadioField("O incremento trouxe avanços significativos para atingir a meta do projeto na totalidade?",
                          choices=[
                          (4,"Sim, o incremento concluiu com o que prometeu no Product Backlog e avança com o valor do produto planejado para as próximas Sprints."),
                          (3,"Parcialmente, o incremento concluiu a maioria dos itens que prometeu no Product Backlog, mas afeta o valor do produto que será remanejado para próximas Sprints."),
                          (2,"Minimamente, o incremento concluiu a minoria dos itens que prometeu no Product Backlog e arrisca o valor do produto planejado para as próximas Sprints. Não atrapalha gravemente o andamento do projeto."),
                          (1,"Não, o incremento não coincide com o prometido e ameaça fortemente a conclusão do projeto conforme a meta e tempo planejados. Há possibilidade de não conseguir entregar ao final de todas as Sprints.")],validators=[DataRequired()])


     incremento_do_produto_p12 = RadioField("O produto entregue está conforme os critérios definidos pela Definição de Pronto?",
                          choices=[
                          (4,"Sim, tudo o que foi pontuado no DoD foi seguido estritamente pela equipe e a qualidade do incremento reflete isso."),
                          (3,"Parcialmente, a minoria dos itens do DoD foram esquecidos, porém, a qualidade do incremento não foi comprometida."),
                          (2,"Minimamente, a maioria dos itens do DoD foram esquecidos e, com isso, a qualidade do incremento foi comprometida, ocasionando em complicações que terão que ser resolvidas na próxima Sprint."),
                          (1,"Não, os itens do DoD não foram seguidos e a qualidade do incremento foi muito comprometida, levando bugs, erros e outras complicações para a próxima Sprint.")],validators=[DataRequired()])
    
     daily_scrum_p19 = RadioField("Nas reuniões de Daily Scrum, foram feitas perguntas para acompanhar o que já foi feito, quais serão os próximos passos e se há impedimentos, para cada membro do Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, todos foram questionados e deram respostas sobre o progresso, planejamento e impedimentos de forma satisfatória."),
                          (3,"Parcialmente, a maioria foi questionada e deu respostas sobre o progresso, planejamento e impedimentos de forma aceitável."),
                          (2,"Minimamente, a minoria foi questionada e deu respostas sobre o progresso, planejamento e impedimentos de forma insatisfatória."),
                          (1,"Não, não foi utilizado nenhuma metodologia de perguntas para acompanhar o progresso, planejamento e impedimentos do time, ocasionando em extrema incerteza sobre o andamento do trabalho.")],validators=[DataRequired()])
    
     daily_scrum_p20 = RadioField("Como você avalia a eficácia das reuniões de Daily Scrum? (Considere se elas mantiveram o foco de acompanhar o progresso do Sprint.)",
                          choices=[
                          (4,"Ótima, todos tiveram abertura e conseguiram comunicar claramente sobre seus progressos, planos e impedimentos, deixando evidente o avanço do time."),
                          (3,"Boa, a maioria teve abertura e conseguiu comunicar claramente sobre seus progressos, planos e impedimentos. Por terem membros que ou não se comunicaram com clareza, ou não tiveram espaço para falar, o avanço do time é perceptível, mas incerto em certas partes."),
                          (2,"Neutra, a minoria teve abertura na conversa e conseguiram comunicar claramente sobre seus progressos, planos e impedimentos. O avanço do time é dificilmente perceptível e há várias incertezas."),
                          (1,"Negativa, nenhuma parte conseguiu se comunicar sobre seus progressos, planos e impedimentos, ocasionando no time estando completamente perdido quanto ao avanço do time.")],validators=[DataRequired()])
    
     sprint_retrospective_p30 = RadioField("Durante a reunião da Sprint Retrospective, os colaboradores da equipe citaram o que ocorreu bem, onde detectaram problemas e as áreas de melhoria?",
                          choices=[
                          (4,"Sim, todos os pontos positivos, fraquezas e áreas de melhoria foram abordados de forma aberta e colaborativa."),
                          (3,"Parcialmente, alguns pontos positivos e problemas foram abordados, mas nem todas as áreas de melhoria foram identificadas."),
                          (2,"Minimamente, poucos pontos foram discutidos, sem aprofundamento em causas ou soluções."),
                          (1,"Não, a equipe não discutiu abertamente os pontos positivos, problemas e nem as áreas de melhoria.")],validators=[DataRequired()])
    
     sprint_retrospective_p31 = RadioField("Todos os integrantes (Product Owner, Scrum Master e Dev Team) conseguiram apresentar suas perspectivas de forma aberta e construtiva?",
                          choices=[
                          (4,"Sim, todos os integrantes apresentaram suas perspectivas ativamente, expressando suas perspectivas com respeito, abertura e foco na melhoria do time."),
                          (3,"Parcialmente, a maioria dos integrantes participou apresentando suas perspectivas, mas houve pouca contribuição ou abertura por parte de alguns membros."),
                          (2,"Minimamente, poucos integrantes apresentaram suas perspectivas, com pouca contribuição aberta e construtiva dentre os membros do time."),
                          (1,"Não, os integrantes não tiveram abertura para expressar suas opiniões de forma construtiva.")],validators=[DataRequired()])
    
     sprint_retrospective_p32 = RadioField("Houve uma boa concordância e uniformidade nas respostas de cada um? Ou cada membro pareceu ter uma perspectiva diferente do que deu ou não, certo?",
                          choices=[
                          (4,"Sim, os membros do grupo compartilham percepções semelhantes sobre o que foi realizado corretamente e sobre o que ainda pode ser aprimorado."),
                          (3,"Parcialmente, alguns membros apresentaram pontos semelhantes sobre o que foi feito corretamente e ao que ainda precisa ser aprimorado, enquanto outros demonstraram pontos de vista diferentes."),
                          (2,"Minimamente, apesar de haver concordância entre as respostas, a maioria apresentou percepções distintas sobre o que foi realizado corretamente e sobre os pontos que precisam de melhoria."),
                          (1,"Não, os membros do grupo demonstraram perspectivas totalmente distintas sobre o que foi bem realizado e sobre os pontos que podem melhorar.")],validators=[DataRequired()])
    
     sprint_retrospective_p33 = RadioField("Houve uma participação ativa de todos os membros na reunião?",
                          choices=[
                          (4,"Sim, todos os membros do grupo mostraram proatividade em compartilhar ideias, expressar pontos de vista e contribuírem de forma ativa para as decisões do grupo."),
                          (3,"Parcialmente, a maioria dos membros se mostrou ativo para compartilhar suas perspectivas, mas alguns não tiveram a mesma participação."),
                          (2,"Minimamente, poucos membros do grupo compartilharam suas ideias e perspectivas, mas ainda houve participação ativa entre alguns."),
                          (1,"Não, nenhum membro do grupo se mostrou proativo a participar e compartilhar suas perspectivas e contribuir ativamente.")],validators=[DataRequired()])
    
     burnup_p38 = RadioField("Como você avalia a utilização do gráfico de Burnup para o acompanhamento da conclusão das Sprints ao longo do projeto todo?",
                          choices=[
                          (4,"O gráfico de Burnup foi utilizado de forma eficaz para acompanhar a conclusão das Sprints ao longo do projeto, permitindo que o time visualizasse de forma clara o progresso e identificasse se estava dentro do planejamento."),
                          (3,"O gráfico de Burnup ajudou na visualização do progresso do projeto e acompanhamento das Sprints, embora em alguns momentos a interpretação dos dados pudesse ser melhorada."),
                          (2,"A utilização do gráfico de Burnup teve impacto limitado, sendo pouco utilizado para monitorar a conclusão das Sprints ou para tomar decisões de planejamento."),
                          (1,"O gráfico de Burnup não foi utilizado de forma adequada, dificultando a visualização do progresso das Sprints e comprometendo o acompanhamento do avanço do projeto.")],validators=[DataRequired()])
    
    
      
    sprint_backlog_p1 = RadioField("As tarefas definidas no Sprint Backlog decorrem dos respectivos itens no Product Backlog?",
                          choices=[
                          (4,"Sim, todas as tarefas são derivadas de pelo menos uma das User Stories programadas para a Sprint em questão."),
                          (3,"Parcialmente, algumas tarefas decorrem de User Stories de Sprints passadas ou futuras, mas a maioria está fiel ao programado para a Sprint."),
                          (2,"Minimamente, a maioria das tarefas estão desconexas com as User Stories definidas previamente, deixando o time confuso sobre o que deve ser entregue."),
                          (1,"Não, nenhuma das tarefas decorrem das User Stories corretas, impossibilitando que o time entregue o MVP referente a Sprint.")],validators=[DataRequired()])
    
    sprint_backlog_p2 = RadioField("A velocidade é definida pela quantidade média de Story points concluídos em uma Sprint. Com base nessa definição, os itens do Sprint Backlog respeitam a métrica do time?",
                          choices=[
                          (4,"Sim, os itens foram definidos o mais próximo possível da média alcançável, tendo qualquer item sobressalente definido como meta complementar às obrigatórias."),
                          (3,"Parcialmente, houve a tentativa de permanecer na média do time, mas devido ao valor prometido, itens a mais foram estabelecidos como meta obrigatória."),
                          (2,"Minimamente, ou a quantidade de Story Points está consideravelmente acima da média, arriscando a conclusão do prometido para Sprint. Ou, a quantidade de Story Points está consideravelmente abaixo da média e não foram adicionados mais itens para evitar períodos de zero produtividade"),
                          (1,"Não, a média não foi considerada em nenhum momento e a quantidade de Story Points está muito acima ou muito abaixo da média, arriscando a entrega do produto inteiro e a qualidade das próximas Sprints.")],validators=[DataRequired()])
    
    sprint_backlog_p3 = RadioField("A Sprint possui um MVP (Produto mínimo viável) bem estabelecido?",
                          choices=[
                          (4,"Sim, o MVP pode ser enxergado claramente tanto pelas tarefas abordadas no Sprint Backlog, quanto explicado mais a fundo em algum outro tipo de documento. A equipe tem plena consciência do que deve ser entregue."),
                          (3,"Parcialmente, o MVP pode ser enxergado nas tarefas abordadas do Sprint Backlog, porém não está registrado explicitamente em nenhum lugar. A equipe tem bom conhecimento sobre o que deve ser entregue."),
                          (2,"Minimamente, o MVP pode ser vagamente observado nas tarefas e não está registrado em nenhum outro local. A equipe está consideravelmente perdida em relação ao que foi prometido."),
                          (1,"Não, o MVP não é claro por meio da escolha das tarefas e não está anotado em nenhum lugar. A equipe não sabe o que deve ser entregue.")],validators=[DataRequired()])
    
    sprint_backlog_p4 = RadioField("As tarefas selecionadas possuem prioridade, User Story e estimativas (Story Points) bem definidas?",
                          choices=[
                          (4,"Sim, as tarefas listadas no Sprint Backlog possuem cada um dos itens mencionados, escritos de forma clara e concisa."),
                          (3,"Parcialmente, quase todas estão padronizadas e alguns itens estão mais concisos e bem escritos do que outros."),
                          (2,"Minimamente, a lista foi feita seguindo um padrão diferente, porém ainda mantém os itens principais: User Story e Story Points."),
                          (1,"Não, a lista está despadronizada e segue algo único e pensado pela própria equipe ao invés das normas especificadas.")],validators=[DataRequired()])
    
    dod_p1 = RadioField(" A Definition of Done têm critérios de aceitação bem definidos para considerar um item pronto?",
                          choices=[
                          (4,"Sim, foram definidos critérios de aceitação bem específicos, objetivos e inquestionáveis, levando a uma fácil compreensão sobre o que se considerou pronto."),
                          (3,"Parcialmente, foram definidos critérios de aceitação específicos, objetivos, mas questionáveis, levando a algumas dúvidas sobre o que se considerou pronto."),
                          (2,"Minimamente, foram definidos critérios nada específicos, não objetivos e questionáveis, levando a uma dificuldade de compreensão sobre o que se considera pronto."),
                          (1,"Não, não foram definidos critérios de aceitação sobre a DoD, ocasionando total falta de consenso no que seria considerado pronto")],validators=[DataRequired()])
    
    dod_p2 = RadioField("A Definition of Done foi acordada formalmente entre o Product Owner e o Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, o Product Owner e o time desenvolveram os critérios em conjunto, deixando a DoD documentada e de fácil acesso a todos."),
                          (3,"Parcialmente, uma das partes teve mais poder de decisão do que a outra, porém a DoD foi documentada e de fácil acesso a todos."),
                          (2,"Minimamente, apenas uma das partes decidiu os critérios para a DoD, em que ela não está claramente documentada e não está de fácil acesso a todos."),
                          (1,"Não, apenas uma das partes decidiu os critérios, a DoD não está documentada, sendo lembrada por meio de acordos verbais, gerando grandes chances do filtro ser completamente ignorado e vários itens não prontos serem aprovados.")],validators=[DataRequired()])
    
    dod_p3 = RadioField("O DoR foi seguido corretamente pela equipe de desenvolvimento?",
                          choices=[
                          (4,"Sim, todos tiveram uma clara compreensão e conseguiram seguir os critérios para definir itens como preparado corretamente."),
                          (3,"Parcialmente, a maioria teve uma boa compreensão e conseguiu seguir os critérios para definir itens como preparado de forma aceitável, mas não excelente."),
                          (2,"Minimamente, a minoria compreendeu e dificilmente conseguiu seguir os critérios para definir itens como preparado, tendo alguns itens definidos incorretamente."),
                          (1,"Não, não houve compreensão e não foi possível seguir os critérios para definir itens como preparado corretamente.")],validators=[DataRequired()])
    
    
    sprint_review_p1 = RadioField("As partes interessadas forneceram feedback sobre o incremento apresentado?",
                          choices=[
                          (4,"Sim, as partes interessadas forneceram feedback claro e construtivo sobre o incremento, contribuindo significativamente para melhorias no produto"),
                          (3,"Parcialmente, o feedback das partes interessadas foi fornecido acerca do incremento, mas de forma pouco objetiva ou pouco detalhada."),
                          (2,"Minimamente, houve pouco feedback das partes interessadas sobre o incremento, sem contribuições relevantes para sua melhoria."),
                          (1,"Não, as partes interessadas não forneceram feedback sobre o incremento apresentado, resultando em incerteza sobre o nível de satisfação.")],validators=[DataRequired()])
    
    sprint_review_p2 = RadioField("Os resultados do Sprint estão bem alinhados à visão do produto e ao objetivo definido? Houve impedimentos significativos que afetaram essas entregas?",
                          choices=[
                          (4,"Sim, os resultados do Sprint estão totalmente alinhados à visão do produto e ao objetivo definido. Não houve impedimentos significativos durante o trabalho."),
                          (3,"Parcialmente, os resultados do Sprint estão em boa parte alinhados à visão do produto e ao objetivo definido. Mas alguns impedimentos afetaram pequenas entregas e detalhes."),
                          (2,"Minimamente, os resultados do Sprint ficaram pouco alinhados com a visão do produto e o objetivo definido. Houve impedimentos relevantes que afetaram a entrega."),
                          (1,"Não, os resultados do Sprint estão desalinhados com a visão do produto e com o objetivo definido. Houve fortes impedimentos que comprometeram significativamente a entrega.")],validators=[DataRequired()])
    
    sprint_review_p3 = RadioField("No caso de itens não concluídos, o Product Backlog foi atualizado de acordo?",
                          choices=[
                          (4,"Sim, o Product Backlog foi atualizado de acordo, refletindo fielmente o estado atual dos itens não concluídos"),
                          (3,"Parcialmente, o Product Backlog foi atualizado de acordo, mas alguns ajustes ou itens ficaram pendentes de revisão."),
                          (2,"Minimamente, o Product Backlog foi atualizado de forma incompleta, com diversas informações desatualizadas."),
                          (1,"Não, o Product Backlog não foi atualizado, afetando a transparência e o planejamento das próximas Sprints.")],validators=[DataRequired()])
    
    sprint_review_p4 = RadioField("Com base no ritmo do time e nas funcionalidades restantes, a previsão de entrega para o Produto Final ainda é realista?",
                          choices=[
                          (4,"Sim, a previsão de entrega continua realista, considerando o ritmo de trabalho atual e as atividades restantes."),
                          (3,"Parcialmente, a previsão de entrega ainda é realista, mas há riscos que podem comprometer o prazo se não receberem atenção e serem tratados."),
                          (2,"Minimamente, a previsão de entrega parece pouco realista, e o ritmo de trabalho do time precisa se ajustar para evitar atrasos."),
                          (1,"Não, a previsão de entrega não parece mais realista, exigindo um replanejamento e revisão do trabalho acerca do produto.")],validators=[DataRequired()])
    
    burndown_p1 = RadioField("O gráfico apresenta uma linha de progresso ideal, dedicada a guiar o tempo em que as tarefas são concluídas até o final do Sprint?",
                          choices=[
                          (4,"Sim, o gráfico apresenta uma linha de progresso ideal, que serve como referência para guiar o ritmo em que as tarefas devem ser concluídas ao longo do Sprint."),
                          (3,"Parcialmente, nem todas as tarefas ou prazos refletem com precisão o ritmo planejado."),
                          (2,"Minimamente, o gráfico mostra apenas alguns pontos de referência do progresso ideal, dificultando que o time o use como guia consistente para acompanhar a conclusão das tarefas."),
                          (1,"Não, o gráfico não apresenta uma linha de progresso ideal clara, impedindo que o time tenha uma referência eficaz para acompanhar o andamento das tarefas até o final do Sprint.")],validators=[DataRequired()])
    
    burndown_p2 = RadioField("Ao longo do Sprint, no BurnDown Chart, como você avalia a linha de conclusão do trabalho real com a linha de conclusão ideal estabelecida?",
                          choices=[
                          (4,"A linha de conclusão do trabalho real acompanhou a linha ideal, mostrando que o Sprint seguiu o planejamento previsto e que o time conseguiu cumprir as tarefas dentro do prazo."),
                          (3,"A linha de conclusão do trabalho real apresentou um desempenho próximo da linha ideal, com pequenas variações."),
                          (2,"A linha de conclusão do trabalho real divergiu de forma considerável da linha ideal em alguns momentos."),
                          (1,"A linha de conclusão do trabalho real apresentou grandes diferenças em relação à linha ideal, mostrando que o planejamento do Sprint não foi seguido corretamente e que o time enfrentou dificuldades para concluir as tarefas no prazo.")],validators=[DataRequired()])
    product_backlog_p1 = RadioField("As tarefas foram priorizadas a partir da dor do cliente?",
                          choices=[
                          (4,"Sim e todos os itens seguem uma ordem de prioridade definida a partir dos princípios e feedbacks do cliente."),
                          (3,"Parcialmente, a maioria dos itens está priorizada no ponto de vista do cliente, porém um item ou outro leva em conta requisitos na perspectiva de desenvolvimento ao invés do que traz maior valor de produto."),
                          (2,"Minimamente, a minoria parte da dor do cliente, enquanto outras pela ótica do desenvolvimento e as outras que deveriam ser incluídas foram esquecidas."),
                          (1,"Não foram respeitadas as dores do cliente, levando a um Product Backlog inconciso e incerto quanto ao MVP.")],coerce=int,validators=[DataRequired()])
    
    product_backlog_p2 = RadioField("Os itens do Product Backlog seguem o padrão de Id, User Story, Descrição, Prioridade e Estimativa?",
                          choices=[
                          (4,"Sim, as tarefas listadas no Product Backlog possuem cada um dos itens mencionados, escritos de forma clara e concisa."),
                          (3,"Parcialmente, quase todas estão padronizadas e alguns itens estão mais concisos e bem escritos do que outros."),
                          (2,"Minimamente, a lista foi feita seguindo um padrão diferente, porém ainda mantém os itens principais: User Story, Descrição e Prioridade."),
                          (1,"Não, a lista está despadronizada e segue algo único e pensado pela própria equipe ao invés das normas especificadas.")],validators=[DataRequired()])
    
    product_backlog_p3 = RadioField("As User Stories têm uma definição clara de seus objetivos?",
                          choices=[
                          (4,"Sim, as histórias foram escritas claramente e seguem o padrão: Como <usuário>, quero <funcionalidade> para <finalidade>."),
                          (3,"Parcialmente, algumas histórias ficaram confusas, permitindo interpretações levemente diferentes dos membros. Contudo, seguem o padrão especificado."),
                          (2,"Minimamente, a maioria das histórias são confusas, permitindo várias interpretações diferentes. Algumas seguem o padrão, enquanto outras fogem."),
                          (1,"Não, todas as histórias estão confusas e mal escritas, deixando o time desorientado sobre o caminho a seguir. Não seguem o padrão em nenhum dos itens listados.")],
                          validators=[DataRequired()])
    
    product_backlog_p4 = RadioField("Houve mudanças decorrentes de conversas com o cliente? Se sim, o Product Backlog foi atualizado corretamente a partir do novo feedback?",
                          choices=[
                          (4,"Mudanças existiram e o Product Backlog foi alterado de acordo, com os novos itens seguindo o padrão corretamente. "),
                          (3,"O Product Backlog não possui todas as atualizações conversadas. Porém, os itens adicionados continuam seguindo o padrão corretamente. "),
                          (2,"Não houveram mudanças e o Product Backlog não precisou ser alterado, mantendo a qualidade que já possuía."),
                          (1,"O Product Backlog não foi alterado, mesmo com atualizações pendentes. Permaneceu o mesmo até o fim da Sprint. ")],validators=[DataRequired()])
   

    dor_p1 = RadioField("A Definition of Ready têm critérios específicos, mensuráveis e atingíveis para considerar um item preparado?",
                          choices=[
                          (4,"Sim, todos os critérios da DoR são específicos, mensuráveis e atingíveis, proporcionando total clareza e objetividade para os membros do time."),
                          (3,"Parcialmente, a maioria dos critérios são específicos, mas existem itens subjetivos, gerando o risco de debates durante a checagem."),
                          (2,"Minimamente, a maioria dos critérios é vago e não mensurável. A DoR foi feita, mas raramente é checada."),
                          (1,"Não, os critérios são completamente subjetivos e a equipe está perdida. Ou a DoR é ignorada ou nem foi feita pelo time.")]
                          ,validators=[DataRequired()])
    
    
    dor_p2 = RadioField("A Definition of Ready foi acordada formalmente entre o Product Owner e o Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, o Product Owner e o time desenvolveram os critérios em conjunto, deixando a DoR documentada e de fácil acesso a todo"),
                          (3,"Parcialmente, uma das partes teve mais poder de decisão do que a outra, porém a DoR foi documentada e de fácil acesso a todos."),
                          (2,"Minimamente, apenas uma das partes decidiu os critérios para a DoR, em que ela não está claramente documentada e não está de fácil acesso a todos"),
                          (1,"Não, apenas uma das partes decidiu os critérios, a DoR não está documentada, sendo lembrada por meio de acordos verbais, gerando grandes chances do filtro ser completamente ignorado e vários itens não preparados serem aprovados.")],validators=[DataRequired()])
    
    dor_p3 = RadioField("O DoR foi seguido corretamente pela equipe de desenvolvimento?",
                          choices=[
                          (4,"Sim, todos tiveram uma clara compreensão e conseguiram seguir os critérios para definir itens como preparado corretamente."),
                          (3,"Parcialmente, a maioria teve uma boa compreensão e conseguiu seguir os critérios para definir itens como preparado de forma aceitável, mas não excelente."),
                          (2,"Minimamente, a minoria compreendeu e dificilmente conseguiu seguir os critérios para definir itens como preparado, tendo alguns itens definidos incorretamente"),
                          (1,"Não, não houve compreensão e não foi possível seguir os critérios para definir itens como preparado corretamente.")],validators=[DataRequired()])
   

    
    sprint_planning_p1 = RadioField("Na reunião, foram definidos quais itens do Product Backlog seriam realizados na Sprint?",
                          choices=[
                          (4,"Sim, os itens do Product Backlog que seriam selecionados para a Sprint foram definidos de forma clara e objetiva, não gerando dúvidas."),
                          (3,"Parcialmente, os itens do Product Backlog que seriam selecionados para a Sprint não foram definidos com excelência, mas foi possível ter uma compreensão boa, sem muitas dúvidas."),
                          (2,"Minimamente, os itens do Product Backlog que seriam selecionados para a Sprint não foram definidos corretamente, gerando pouca compreensão e muitas dúvidas."),
                          (1,"Não, não foram definidos os itens do Product Backlog a serem selecionados para a Sprint, gerando grande incompreensão e falta de organização.")],
                          validators=[DataRequired()])
    
    sprint_planning_p2 = RadioField("As tarefas foram planejadas devidamente?",
                          choices=[
                          (4,"Sim, as tarefas foram planejadas considerando os itens do Product Backlog que devem ser priorizados, bem como quais serão os itens entregáveis para a Sprint e se existem riscos e dependências entre eles."),
                          (3,"Parcialmente, as tarefas consideraram a maioria dos itens marcados como prioridade no Product Backlog, excluindo alguns itens de pouca prioridade. Foram definidos os itens entregáveis, mas a análise de riscos e dependências foi pouco discutida."),
                          (2,"Minimamente, as tarefas desconsideraram algumas prioridades médias e várias das baixas. Itens que deveriam entrar como entregáveis foram esquecidos e a análise de riscos foi extremamente breve ou inexistente."),
                          (1,"Não, as tarefas selecionadas não levaram em conta quais itens deveriam ser priorizados do Product Backlog, muito menos os itens entregáveis e os riscos e dependências entre eles; resultando em uma Sprint com promessas confusas.")],validators=[DataRequired()])
    
    sprint_planning_p3 = RadioField("Como você avalia a forma como foi feita a divisão das tarefas?",
                          choices=[
                          (4,"Ótima, as tarefas foram bem distribuídas, considerando a capacidade e habilidade de cada membro, favorecendo o equilíbrio do time e o cumprimento dos prazos."),
                          (3,"Boa, a maioria das tarefas foram distribuídas considerando a capacidade e habilidade de cada membro e, como certas tarefas foram mal pensadas, uma pequena parte dos colaboradores tem mais trabalho e responsabilidades."),
                          (2,"Neutra, a maioria das tarefas foram distribuídas sem considerar a capacidade e habilidade de cada membro e, com isso, vários colaboradores se viram sobrecarregados de trabalho."),
                          (1,"Ruim, as tarefas foram mal distribuídas, muitos membros ficaram sobrecarregados enquanto outros tiveram pouca participação e ficaram ociosos.")],validators=[DataRequired()])
    
    sprint_planning_p4 = RadioField("Os itens selecionados do Product Backlog atendiam ao DoR definido antes do início do planejamento?",
                          choices=[
                          (4,"Sim, todos os itens selecionados do Product Backlog atenderam ao DoR definido, apresentando critérios claros, compreensíveis e prontos para execução."),
                          (3,"Parcialmente, a maioria dos itens selecionados do Product Backlog atendeu ao DoR definido, mas alguns apresentaram dúvidas que precisaram ser resolvidas durante a Sprint."),
                          (2,"Minimamente, poucos itens selecionados do Product Backlog atenderam ao DoR definido, ocasionando grandes incertezas e retrabalho durante a execução."),
                          (1,"Não, os itens selecionados do Product Backlog não atenderam ao DoR definido, comprometendo a clareza e o andamento do Sprint.")],validators=[DataRequired()])
    
    
    story_point_p1 = RadioField("As Story Points foram definidas de acordo com as estimativas de esforço entre os membros do Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, todas as Story Points foram definidas de acordo com as estimativas de esforço compartilhadas pelos membros do Time de Desenvolvimento."),
                          (3,"Parcialmente, a maioria das Story Points foram definidas com as estimativas de esforço entre os membros do Time de Desenvolvimento, mas houveram outras que foram definidas por perspectivas individuais."),
                          (2,"Minimamente, poucas Story Points foram definidas de acordo com as estimativas do Time de Desenvolvimento."),
                          (1,"Não, as Story Points não foram definidas de acordo com as estimativas do Time de Desenvolvimento, sendo determinadas sem consenso ou alinhamento entre os membros.")],validators=[DataRequired()])
    
    
    story_point_p2 = RadioField(" Como você avalia a utilização das métricas de estimativa em seus Backlogs?",
                          choices=[
                          (4,"As métricas de estimativa foram utilizadas de forma consistente e eficaz, permitindo que o Time de Desenvolvimento planejasse e priorizasse as tarefas do Backlog com clareza e precisão."),
                          (3,"As métricas de estimativa foram úteis na maior parte do tempo, auxiliando o planejamento do Backlog, embora algumas tarefas possam não ter sido estimadas com total precisão."),
                          (2,"A utilização das métricas de estimativa apresentou resultados medianos, sem grande impacto no planejamento do Backlog."),
                          (1,"As métricas de estimativa foram pouco e/ou mal utilizadas, dificultando o planejamento e a priorização das tarefas do Backlog, atrapalhando o acompanhamento do progresso do Sprint.")],validators=[DataRequired()])
   
    
 
    
    
 




