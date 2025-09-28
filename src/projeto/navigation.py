navigation_items = [
  {
    "topic": { "name": "Visão Geral", "solo_item": False },
    "subtopic": [
      {
        "name": "Metodologia Scrum",
        "endpoint": "scrum",
        "sub_navigation": [
          "O que é o Scrum?",
          "Os benefícios do Srcum",
          "Porque o Scrum é uma boa escolha?"
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
       {
        "name": "Valores do Scrum",
        "endpoint": "valores",
        "sub_navigation": None,
      },
     
    ],
    "initialState": "true"
  },
  {
    "topic": { "name": "Papéis", "solo_item": True },
     "subtopic": [{"endpoint": "papeis", "sub_navigation": ["Product Owner", "Scrum Master", "Dev Team"]}],
  },
   {
    "topic": { "name": "Artefatos", "solo_item": False },
    "subtopic": [
      {
        "name": "Product Backlog",
        "endpoint": "productBacklog",
        "sub_navigation": None,
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
        "sub_navigation": ["O que é uma Sprint?", "Entendendo a Analogia do Bolo"],
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
        "sub_navigation":["Story Point", "Para que serve estimar?", "Velocidade",],
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