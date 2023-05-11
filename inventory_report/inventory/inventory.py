import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_csv(file):
    return list(csv.DictReader(file))


def read_json(file):
    data = file.read()
    return json.loads(data)


def read_file(file_path):
    with open(file_path) as file:
        if file_path.endswith(".csv"):
            return read_csv(file)
        elif file_path.endswith(".json"):
            return read_json(file)


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        data = read_file(file_path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
