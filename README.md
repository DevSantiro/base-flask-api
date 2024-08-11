```
/project-root
│
├── /app
│   ├── /api_v1                      # Versão 1 da API
│   │   ├── /app                     # Arquivo inicial do Flask (App)
│   │   │   ├── __init__.py
│   │   ├── /controllers             # Controladores (lógica dos endpoints)
│   │   │   ├── __init__.py
│   │   │   └── user_controller.py   # Exemplo de controlador
│   │   ├── /models                  # Modelos de dados (ORM ou consultas SQL)
│   │   │   ├── __init__.py
│   │   │   └── user_model.py        # Exemplo de modelo
│   │   ├── /services                # Serviços de negócio
│   │   │   ├── __init__.py
│   │   │   └── user_service.py      # Exemplo de serviço
│   │   ├── /schemas                 # Schemas para validação de dados (opcional)
│   │   │   ├── __init__.py
│   │   │   └── user_schema.py       # Exemplo de schema
│   │   ├── /utils                   # Utilitários e funções comuns
│   │   │   ├── __init__.py
│   │   │   └── db_utils.py          # Exemplo de utilitário de banco de dados
│   │   ├── /migrations              # Scripts de migração do banco de dados
│   │   │   ├── __init__.py
│   │   │   └── 01_initial.sql       # Exemplo de script de migração
│   │   ├── /config                  # Configurações da aplicação
│   │   │   ├── __init__.py
│   │   │   └── config.py            # Configurações específicas por ambiente
│   │   ├── /extensions              # Extensões do Flask (como conexões com BD)
│   │   │   ├── __init__.py
│   │   │   └── database.py          # Inicialização e configuração do banco de dados
│   │   ├── /middlewares             # Middlewares da aplicação
│   │   │   ├── __init__.py
│   │   │   └── auth_middleware.py   # Exemplo de middleware de autenticação
│   │   └── routes.py                # Definição das rotas da API
│   │
│   ├── /api_v2                      # Versão 2 da API (similar à v1)
│   │   ├── ...
│   │
│   └── __init__.py                  # Inicialização da aplicação
│
├── /tests                           # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_user_controller.py      # Exemplo de teste de controlador
│   └── ...
│
├── /scripts                         # Scripts de automação e manutenção
│   ├── __init__.py
│   ├── manage.py                    # Script de gerenciamento (ex: rodar servidor)
│   └── ...
│
├── /docs                            # Documentação da API
│   └── openapi.yaml                 # Especificação OpenAPI
│
├── .env                             # Variáveis de ambiente
├── .gitignore                       # Arquivos e pastas a ignorar pelo Git
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação do projeto
```

### Descrição dos Diretórios:

- **/app**: Diretório principal que contém a aplicação Flask.
- **/api_v1**: Contém a primeira versão da API, com subdiretórios para controllers, models, services, etc.
- **/controllers**: Lógica dos endpoints.
- **/models**: Definição de modelos de dados e/ou consultas SQL.
- **/services**: Implementação das regras de negócio.
- **/schemas**: Schemas para validação de dados de entrada e saída (opcional).
- **/utils**: Funções utilitárias e helpers.
- **/migrations**: Scripts de migração do banco de dados.
- **/config**: Configurações da aplicação por ambiente.
- **/extensions**: Inicialização de extensões do Flask, como a conexão com o banco de dados.
- **/middlewares**: Middlewares da aplicação, como autenticação.
- **routes.py**: Mapeamento das rotas da API.
- **/tests**: Testes unitários e de integração.
- **/scripts**: Scripts de manutenção e automação.
- **/docs**: Documentação da API, como especificação OpenAPI.
