from flask import Flask, render_template, abort

app = Flask(__name__)

# Base de dados simulada em memória (Catálogo de Serviços)
SERVICOS = [
    {
        "id": 1,
        "nome": "Revisão Completa de Freios",
        "preco": "R$ 380,00",
        "tempo": "2 horas",
        "descricao": "Substituição de pastilhas dianteiras, limpeza do sistema, sangria e troca do fluido DOT 4.",
        "garantia": "6 meses"
    },
    {
        "id": 2,
        "nome": "Troca de Óleo e Filtros",
        "preco": "R$ 260,00",
        "tempo": "1 hora",
        "descricao": "Óleo 5W30 100% sintético (4 litros) + substituição do filtro de óleo, ar do motor e cabine.",
        "garantia": "10.000 km ou 6 meses"
    },
    {
        "id": 3,
        "nome": "Alinhamento 3D e Balanceamento",
        "preco": "R$ 150,00",
        "tempo": "1 hora",
        "descricao": "Alinhamento computadorizado de direção, cambagem básica e balanceamento das 4 rodas.",
        "garantia": "3 meses"
    },
    {
        "id": 4,
        "nome": "Diagnóstico Eletrônico via Scanner",
        "preco": "R$ 180,00",
        "tempo": "1h30",
        "descricao": "Leitura completa da ECU (injeção eletrônica, ABS, Airbag), limpeza de códigos de falha e teste de bicos.",
        "garantia": "3 meses"
    }
]

# Base simulada de Ordens de Serviço por Placa
ORDENS_SERVICO = {
    "ABC1D23": {
        "veiculo": "VW Golf GTI 2.0 TSI",
        "cliente": "Carlos Eduardo",
        "status": "Em manutenção (Elevador 2)",
        "servico_atual": "Revisão Completa de Freios + Diagnóstico via Scanner",
        "previsao_entrega": "Hoje às 17:30",
        "total": "R$ 560,00"
    },
    "XYZ9K88": {
        "veiculo": "Honda Civic Touring 1.5 Turbo",
        "cliente": "Fernanda Souza",
        "status": "Pronto para retirada",
        "servico_atual": "Troca de Óleo e Filtros",
        "previsao_entrega": "Concluído",
        "total": "R$ 260,00"
    }
}

# --- ROTAS FIXAS ---

@app.route("/")
def index():
    return render_template("index.html", servicos=SERVICOS[:2], os_exemplos=ORDENS_SERVICO.keys())

@app.route("/servicos")
def listar_servicos():
    return render_template("servicos.html", servicos=SERVICOS)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# --- ROTAS DINÂMICAS ---

@app.route("/servico/<int:id>")
def detalhe_servico(id):
    servico = next((s for s in SERVICOS if s["id"] == id), None)
    if not servico:
        abort(404)
    return render_template("detalhe_servico.html", servico=servico)

@app.route("/os/<placa>")
def consultar_os(placa):
    placa_formatada = placa.upper()
    ordem = ORDENS_SERVICO.get(placa_formatada)
    return render_template("ordem_servico.html", placa=placa_formatada, ordem=ordem)

if __name__ == "__main__":
    app.run(debug=True)
