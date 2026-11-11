# AutoTech Oficina & Gerenciamento

Portal web em **Flask** para uma oficina mecânica: catálogo de serviços e ordens de serviço (OS), com banco de dados **SQLite** e SQL nativo.

## Estrutura

```
oficina_flask/
├── app.py            # Rotas
├── db_sql.py         # Conexão, comandos SQL e comando "flask init-db"
├── schema.sql        # Criação das tabelas e dados de exemplo
├── requirements.txt
└── templates/
```

## Como executar

```bash
python -m venv .venv
.venv\Scripts\activate        # Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask init-db
python -m flask run
```

Acesse: http://127.0.0.1:5000

## Banco de dados

- `servicos`: catálogo de serviços
- `ordens_servico`: ordens de serviço, ligadas a um serviço por `servico_id`

Relacionamento **1:N**: um serviço pode estar em várias ordens de serviço.
A chave estrangeira usa `ON DELETE SET NULL`: se um serviço for excluído, a OS continua existindo, mas sem serviço vinculado.

## Rotas

| Rota | Descrição |
|---|---|
| `/` | Página inicial |
| `/servicos` | Lista de serviços |
| `/servico/<id>` | Detalhe de um serviço |
| `/servicos/novo` | Cadastrar serviço |
| `/servico/<id>/editar` | Editar serviço |
| `/servico/<id>/excluir` | Excluir serviço |
| `/ordens` | Lista de ordens de serviço |
| `/ordens/nova` | Cadastrar OS |
| `/ordem/<id>/editar` | Editar OS |
| `/ordem/<id>/excluir` | Excluir OS |
| `/os/<placa>` | Consultar OS pela placa |
| `/sobre` | Sobre a oficina |

Placas de teste: `ABC1D23` e `XYZ9K88`.
