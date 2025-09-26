navigation_items = [
    {
    "topic": { "name": "Template de Conteúdo", "solo_item": True },
    "subtopic": [{"endpoint": "template", "sub_navigation": ["Texto simples", "Conteúdo Listado - ex1", "Conteúdo Listado - ex2", "Conteúdo Listado - ex3", "Imagens"]}],
  },
  {
    "topic": { "name": "Visão Geral", "solo_item": False },
    "subtopic": [
      {
        "name": "Metodologia Scrum",
        "endpoint": "scrum",
        "sub_navigation": [
          "Definição",
          "Importância",
        ],
      },
      {
        "name": "Manifesto para Desenvolvimento Ágil",
        "endpoint": "manifestoAgil",
        "sub_navigation": None,
      },
      {
        "name": "Princípios Ágeis",
        "endpoint": "principiosAgeis",
        "sub_navigation": None,
      },
     
    ],
    "initialState": "true"
  },
  {
    "topic": { "name": "Papéis", "solo_item": False },
    "subtopic": [
      {
        "name": "Product Owner",
        "endpoint": "productOwner",
        "sub_navigation": None,
      },
      {
        "name": "Scrum Master",
        "endpoint": "scrumMaster",
        "sub_navigation": None,
      },
      {
        "name": "Dev Team",
        "endpoint": "devTeam",
        "sub_navigation": None,
      },
    ],
  },
   {
    "topic": { "name": "Artefatos", "solo_item": False },
    "subtopic": [
      {
        "name": "Product Backlog",
        "endpoint": "productBacklog",
        "sub_navigation": ["User Stories"],
      },
      {
        "name": "Sprint Backlog",
        "endpoint": "sprintBacklog",
        "sub_navigation": None,
      },
      {
        "name": "Incremento do Produto",
        "endpoint": "incrementoProduto",
        "sub_navigation": None,
      },
    ],
  },
  {
    "topic": { "name": "Definition of Ready", "solo_item": True },
    "subtopic": [{"endpoint": "definitionOfReady", "sub_navigation": None}],
  },
  {
    "topic": { "name": "Definition of Done", "solo_item": True },
    "subtopic": [{"endpoint": "definitionOfDone", "sub_navigation": None }],
  },
    {
    "topic": { "name": "Eventos", "solo_item": False },
    "subtopic": [
      {
        "name": "Dailly Scrum",
        "endpoint": "daillyScrum",
        "sub_navigation": None,
      },
      {
        "name": "Sprints",
        "endpoint": "sprints",
        "sub_navigation": None,
      },
      {
        "name": "Sprint Planning",
        "endpoint": "sprintPlanning",
        "sub_navigation": None,
      },
      {
        "name": "Sprint Review",
        "endpoint": "sprintReview",
        "sub_navigation": None,
      },
      {
        "name": "Sprint Restrospective",
        "endpoint": "sprintRestrospective",
        "sub_navigation": None,
      },
    ],
  },
  {
    "topic": { "name": "Métricas Ágeis", "solo_item": False },
    "subtopic": [
      {
        "name": "Story Point",
        "endpoint": "storyPoint",
        "sub_navigation": None,
      },
      {
        "name": "BurnDown chart",
        "endpoint": "burnDownChart",
        "sub_navigation": None,
      },
      {
        "name": "BurnUp chart",
        "endpoint": "burnUpChart",
        "sub_navigation": None,
      },
    ],
  },
 
 
]