navigation_items = [
  {
    "topic": { "name": "Primeiros Passos", "solo_item": False },
    "subtopic": [
      {
        "name": "Metodologia Scrum",
        "endpoint": "scrum",
        "sub_navigation": [
          "Definição",
          "Importância",
          "Manifesto",
          "Princípios Ágeis",
        ],
      },
    ],
    "initialState": "true"
  },
  {
    "topic": { "name": "Sprints", "solo_item": True },
    "subtopic": [{"endpoint": "sprints", "sub_navigation": ["Sprints", "Como funcionam"] }],
  },
  {
    "topic": { "name": "Papéis", "solo_item": False },
    "subtopic": [
      {
        "name": "Product Owner",
        "endpoint": "productOwner",
        "sub_navigation": ["PO", "Como funciona"],
      },
      {
        "name": "Scrum Master",
        "endpoint": "scrumMaster",
        "sub_navigation": ["SM", "Como funciona"],
      },
      {
        "name": "Dev Team",
        "endpoint": "devTeam",
        "sub_navigation": ["DV", "Como funciona"],
      },
    ],
  },
  
]
