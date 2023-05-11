import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        fabricate_dates = [
            datetime.datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            )
            for product in products
        ]
        oldest_fabricate_date = min(fabricate_dates).strftime("%Y-%m-%d")
        nearest_expiration_date = get_nearest_expiration_date(products)
        company_with_most_items = get_company_with_most_items(products)

        report = (
            f"Data de fabricação mais antiga: {oldest_fabricate_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_items}"
        )
        return report


def get_nearest_expiration_date(products):
    valid_products = [
        product
        for product in products
        if is_valid(product["data_de_validade"])
    ]
    if not valid_products:
        return ""

    nearest_expiration_date = min(
        valid_products, key=lambda p: p["data_de_validade"]
    )["data_de_validade"]
    return nearest_expiration_date


def is_valid(expiration_date):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    return expiration_date >= now


def get_company_with_most_items(products):
    company_names = [product["nome_da_empresa"] for product in products]
    company_with_most_items = Counter(company_names).most_common(1)[0][0]
    return company_with_most_items
