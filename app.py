import os
import sqlite3

import click
from flask import (Flask, abort, flash, redirect, render_template,
request, url_for)

import db_sql

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = os.path.join(app.root_path, "oficina.db")
db_sql.init_app(app)

STATUS = ["Aguardando", "Em manutenção", "Pronto para retirada", "Entregue"]

@app.template_filter("brl")
def brl(valor):
    return f"R$ {valor:.2f}".replace(".", ",")

def dados_servico():
    f = request.form
    return f["nome"], float(f["preco"]), f["tempo"], f["descricao"], f["garantia"]

def dados_ordem():
    f = request.form
    return (f["placa"].upper(), f["veiculo"], f["cliente"], f["status"],
            f["previsao_entrega"], float(f["total"]), f["servico_id"] or None)

@app.route("/")
def index():
    return render_template(
        "index.html",
        servicos=db_sql.listar_servicos()
    )

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/servicos")
def listar_servicos():
    return render_template("servicos.html", servicos=db_sql.listar_servicos())

@app.route("/servico/<int:id>")
def detalhe_servico(id):
    servico = db_sql.buscar_servico(id)
    if not servico:
        abort(404)
    return render_template("detalhe_servico.html", servico=servico)

@app.route("/servicos/novo", methods=["GET", "POST"])
def novo_servico():
    if request.method == "POST":
        try:
            db_sql.inserir_servico(*dados_servico())
            flash("Serviço cadastrado!")
            return redirect(url_for("listar_servicos"))
        except sqlite3.IntegrityError:
            flash("Já existe um serviço com esse nome.")
    return render_template("servico_form.html", servico=request.form)

@app.route("/servico/<int:id>/editar", methods=["GET", "POST"])
def editar_servico(id):
    servico = db_sql.buscar_servico(id)
    if not servico:
        abort(404)
    if request.method == "POST":
        try:
            db_sql.atualizar_servico(id, *dados_servico())
            flash("Serviço atualizado!")
            return redirect(url_for("listar_servicos"))
        except sqlite3.IntegrityError:
            flash("Já existe um serviço com esse nome.")
    return render_template("servico_form.html", servico=servico)

@app.route("/servico/<int:id>/excluir", methods=["POST"])
def excluir_servico(id):
    db_sql.excluir_servico(id)
    flash("Serviço excluído.")
    return redirect(url_for("listar_servicos"))

@app.route("/ordens")
def listar_ordens():
    return render_template("ordens.html", ordens=db_sql.listar_ordens())

@app.route("/ordens/nova", methods=["GET", "POST"])
def nova_ordem():
    if request.method == "POST":
        db_sql.inserir_ordem(*dados_ordem())
        flash("Ordem de serviço criada!")
        return redirect(url_for("listar_ordens"))
    return render_template("ordem_form.html", ordem={}, servicos=db_sql.listar_servicos(), status=STATUS)

@app.route("/ordem/<int:id>/editar", methods=["GET", "POST"])
def editar_ordem(id):
    ordem = db_sql.buscar_ordem(id)
    if not ordem:
        abort(404)
    if request.method == "POST":
        db_sql.atualizar_ordem(id, *dados_ordem())
        flash("Ordem de serviço atualizada!")
        return redirect(url_for("listar_ordens"))
    return render_template("ordem_form.html", ordem=ordem, servicos=db_sql.listar_servicos(), status=STATUS)

@app.route("/ordem/<int:id>/excluir", methods=["POST"])
def excluir_ordem(id):
    db_sql.excluir_ordem(id)
    flash("Ordem de serviço excluída.")
    return redirect(url_for("listar_ordens"))

@app.route("/os")
def buscar_os():
    return redirect(url_for("consultar_os", placa=request.args.get("placa", "")))

@app.route("/os/<placa>")
def consultar_os(placa):
    placa = placa.upper()
    return render_template("ordem_servico.html", placa=placa, ordens=db_sql.buscar_ordens_por_placa(placa))

if __name__ == "__main__":
    app.run(debug=True)
