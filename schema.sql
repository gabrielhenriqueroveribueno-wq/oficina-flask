DROP TABLE IF EXISTS ordens_servico;
DROP TABLE IF EXISTS servicos;

CREATE TABLE servicos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT NOT NULL UNIQUE,
    preco     REAL NOT NULL,
    tempo     TEXT NOT NULL,
    descricao TEXT NOT NULL,
    garantia  TEXT NOT NULL
);

CREATE TABLE ordens_servico (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    placa            TEXT NOT NULL,
    veiculo          TEXT NOT NULL,
    cliente          TEXT NOT NULL,
    status           TEXT NOT NULL,
    previsao_entrega TEXT,
    total            REAL NOT NULL,
    servico_id       INTEGER,
    FOREIGN KEY (servico_id) REFERENCES servicos (id) ON DELETE SET NULL
);

INSERT INTO servicos (nome, preco, tempo, descricao, garantia) VALUES
    ('Revisão Completa de Freios', 380, '2 horas', 'Substituição de pastilhas dianteiras, limpeza do sistema, sangria e troca do fluido DOT 4.', '6 meses'),
    ('Troca de Óleo e Filtros', 260, '1 hora', 'Óleo 5W30 100% sintético (4 litros) + substituição do filtro de óleo, ar do motor e cabine.', '10.000 km ou 6 meses'),
    ('Alinhamento 3D e Balanceamento', 150, '1 hora', 'Alinhamento computadorizado de direção, cambagem básica e balanceamento das 4 rodas.', '3 meses'),
    ('Diagnóstico Eletrônico via Scanner', 180, '1h30', 'Leitura completa da ECU (injeção eletrônica, ABS, Airbag), limpeza de códigos de falha e teste de bicos.', '3 meses');

INSERT INTO ordens_servico (placa, veiculo, cliente, status, previsao_entrega, total, servico_id) VALUES
    ('ABC1D23', 'VW Golf GTI 2.0 TSI', 'Carlos Eduardo', 'Em manutenção', 'Hoje às 17:30', 380, 1),
    ('ABC1D23', 'VW Golf GTI 2.0 TSI', 'Carlos Eduardo', 'Em manutenção', 'Hoje às 17:30', 180, 4),
    ('XYZ9K88', 'Honda Civic Touring 1.5 Turbo', 'Fernanda Souza', 'Pronto para retirada', 'Concluído', 260, 2);
