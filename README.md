# 🔧 AutoTech Oficina & Gerenciamento

Portal web em **Flask** para uma oficina mecânica: catálogo de serviços e consulta de Ordens de Serviço (OS) pela placa do veículo.

## 📁 Estrutura

```
oficina_flask/
├── .gitignore
├── requirements.txt
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    ├── servicos.html
    ├── detalhe_servico.html
    ├── ordem_servico.html
    └── sobre.html
```

## 🚀 Como executar

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Rodar a aplicação
python app.py
```

Acesse: http://127.0.0.1:5000

## 🛣️ Rotas

| Tipo      | Rota                 | Descrição                              |
|-----------|----------------------|----------------------------------------|
| Fixa      | `/`                  | Página inicial                         |
| Fixa      | `/servicos`          | Catálogo de serviços                   |
| Fixa      | `/sobre`             | Sobre a oficina                        |
| Dinâmica  | `/servico/<id>`      | Ficha técnica de um serviço            |
| Dinâmica  | `/os/<placa>`        | Consulta de OS pela placa              |

Placas de teste: `ABC1D23` e `XYZ9K88`.

## 🧰 Tecnologias

- Python 3 + Flask
- Jinja2 (herança de templates)
- Bootstrap 5 (via CDN)
