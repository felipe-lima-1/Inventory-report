from inventory_report.inventory.product import Product


def test_relatorio_produto():
    t_products = {
        "id": "1",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-12-22",
        "data_de_validade": "2024-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    }

    products = Product(**t_products)
    expected = (
        f"O produto {t_products['nome_do_produto']}"
        f" fabricado em {t_products['data_de_fabricacao']}"
        f" por {t_products['nome_da_empresa']}"
        f" com validade até {t_products['data_de_validade']}"
        f" precisa ser armazenado {t_products['instrucoes_de_armazenamento']}."
    )

    assert repr(products) == expected
