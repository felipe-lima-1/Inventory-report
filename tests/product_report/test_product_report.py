from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        "1",
        "NITROUS OXIDE",
        "Galena Biopharma",
        "2020-12-22",
        "2024-11-07",
        "CZ09 8588 0858 8435 9140 2695",
        "instrucao 3",
    )

    assert produto.__repr__() == (
        f"O produto {produto.nome_do_produto}"
        f"fabricado em {produto.data_de_fabricacao}"
        f"por {produto.nome_da_empresa}"
        f"com validade até {produto.data_de_validade}"
        f"precisa ser armazenado {produto.instrucoes_de_armazenamento}"
    )
