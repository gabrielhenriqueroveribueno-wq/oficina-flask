import sqlite3

import click
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@click.command("init-db")
def init_db_command():
    with current_app.open_resource("schema.sql") as f:
        get_db().executescript(f.read().decode("utf-8"))
    click.echo("Banco de dados criado.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def executar(sql, params=()):
    db = get_db()
    db.execute(sql, params)
    db.commit()

def listar_servicos():
    return get_db().execute("SELECT * FROM servicos ORDER BY nome").fetchall()

def buscar_servico(id):
    return get_db().execute("SELECT * FROM servicos WHERE id = ?", (id,)).fetchone()

def inserir_servico(nome, preco, tempo, descricao, garantia):
    executar(
        "INSERT INTO servicos (nome, preco, tempo, descricao, garantia) VALUES (?, ?, ?, ?, ?)",
        (nome, preco, tempo, descricao, garantia),
    )

def atualizar_servico(id, nome, preco, tempo, descricao, garantia):
    executar(
        "UPDATE servicos SET nome = ?, preco = ?, tempo = ?, descricao = ?, garantia = ? WHERE id = ?",
        (nome, preco, tempo, descricao, garantia, id),
    )

def excluir_servico(id):
    executar("DELETE FROM servicos WHERE id = ?", (id,))

SELECT_OS = """
    SELECT os.*, s.nome AS servico_nome
    FROM ordens_servico os
    LEFT JOIN servicos s ON s.id = os.servico_id
"""

def listar_ordens():
    return get_db().execute(SELECT_OS + " ORDER BY os.id DESC").fetchall()

def buscar_ordem(id):
    return get_db().execute(SELECT_OS + " WHERE os.id = ?", (id,)).fetchone()

def buscar_ordens_por_placa(placa):
    return get_db().execute(SELECT_OS + " WHERE os.placa = ? ORDER BY os.id DESC", (placa,)).fetchall()

def inserir_ordem(placa, veiculo, cliente, status, previsao_entrega, total, servico_id):
    executar(
        """INSERT INTO ordens_servico (placa, veiculo, cliente, status, previsao_entrega, total, servico_id)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (placa, veiculo, cliente, status, previsao_entrega, total, servico_id),
    )

def atualizar_ordem(id, placa, veiculo, cliente, status, previsao_entrega, total, servico_id):
    executar(
        """UPDATE ordens_servico
           SET placa = ?, veiculo = ?, cliente = ?, status = ?, previsao_entrega = ?, total = ?, servico_id = ?
           WHERE id = ?""",
        (placa, veiculo, cliente, status, previsao_entrega, total, servico_id, id),
    )

def excluir_ordem(id):
    executar("DELETE FROM ordens_servico WHERE id = ?", (id,))
