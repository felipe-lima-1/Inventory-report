from .simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(data):
        company_items = Counter(
            [product["nome_da_empresa"] for product in data]
        )
        company_report = "\nProdutos estocados por empresa:\n"
        for company, count in company_items.items():
            company_report += f"- {company}: {count}\n"
        return SimpleReport.generate(data) + company_report
