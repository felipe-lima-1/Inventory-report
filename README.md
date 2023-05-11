# Inventory Report Generator

O Inventory Report Generator é um projeto em Python que permite gerar relatórios de inventário de produtos a partir de arquivos CSV, JSON e XML. Ele utiliza os conceitos de programação orientada a objetos e padrões de projeto para fornecer uma solução flexível e escalável para gerar relatórios.

## Requisitos

- Python 3.6 ou superior
- Biblioteca json
- Biblioteca xml.etree.ElementTree
- Biblioteca pytest (para testes)

## Instalação

1. Clone ou faça o download do repositório em seu computador.
2. Certifique-se de ter o Python 3.6 ou superior instalado em seu computador. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
3. Instale as bibliotecas json, xml.etree.ElementTree e pytest executando o seguinte comando no terminal:
    
    ```pip install json xml.etree.ElementTree pytest```


## Como usar

1. Crie um arquivo CSV, JSON ou XML com os dados dos produtos a serem incluídos no relatório.
2. Abra o arquivo `report_generator.py` em um editor de texto ou IDE.
3. Crie uma instância da classe `InventoryReportGenerator` passando como argumento o caminho para o arquivo com os dados dos produtos.

    ```report = InventoryReportGenerator('caminho/para/o/arquivo.csv')```


4. Utilize o método `generate_report` para gerar o relatório. Esse método possui dois argumentos opcionais: `output_file` e `report_type`. 

- `output_file` deve conter o caminho para o arquivo onde o relatório de inventário será gerado. Se esse argumento não for passado, o relatório será exibido no console.

- `report_type` deve conter o tipo de relatório a ser gerado: "simple" ou "complete". Se esse argumento não for passado, o relatório completo será gerado.

    ```report.generate_report(output_file='caminho/para/o/arquivo_de_saida.csv', report_type='simple')```


5. O relatório de inventário será gerado no arquivo especificado em `output_file`, ou exibido no console, de acordo com os argumentos passados.

## Testes

Este projeto inclui testes automatizados para garantir que as funções estejam funcionando corretamente. Para rodar os testes, execute o seguinte comando no terminal:

    pytest test_report_generator.py


## Contribuindo

Contribuições são bem-vindas! Se você tiver ideias de como melhorar este projeto, por favor, abra uma issue ou envie um pull request.
