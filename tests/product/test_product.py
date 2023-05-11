from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        "1",
        "NITROUS OXIDE",
        "Galena Biopharma",
        "2020-12-22",
        "2024-11-07",
        "CZ09 8588 0858 8435 9140 2695",
        "instrucao 3",
    )
    assert produto.id == "1"
    assert produto.nome_do_produto == "NITROUS OXIDE"
    assert produto.nome_da_empresa == "Galena Biopharma"
    assert produto.data_de_fabricacao == "2020-12-22"
    assert produto.data_de_validade == "2024-11-07"
    assert produto.numero_de_serie == "CZ09 8588 0858 8435 9140 2695"
    assert produto.instrucoes_de_armazenamento == "instrucao 3"
