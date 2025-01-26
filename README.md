# Extração e organização de dados para o Excel com Python

## Sobre
Este programa tem como objetivo automatizar o processo de extração e organização de dados de um arquivo de texto que contém quantidade, descrição e valor de itens para uma planilha do Excel. O processo envolve a leitura do arquivo e a manipulação do conteúdo com expressões regulares para separar as partes do texto. As informações extraidas são organizadas em dicionários, armazenadas em uma lista e, em seguida, convertidas em um DataFrame para que os dados possam ser exportados de forma organizada para uma planilha do Excel.

Nesse projeto, consegui praticar meus conhecimentos iniciais em Python, utilizando técnicas de leitura e manipulação de arquivos, expressões regulares, tratamento de erros e exceções, funções para modularizar o código e estrutura de dados.

## Bibliotecas

- [re](https://docs.python.org/pt-br/3/library/re.html) - expressões regulares
- [pandas](https://pandas.pydata.org/docs/user_guide/index.html) - organização e exportação dos dados extraídos para um formato de planilha Excel
- [os](https://docs.python.org/pt-br/3.13/library/os.html) - interação com o sistema operacional

## Pré-requisitos

Instalar a biblioteca pandas com a dependência do Excel - necessário ter o Python 3.9 ou superior instalado 

```bash
pip install "pandas[excel]"
```

## Contribuição
Contribuições para ampliar as funcionalidades da código são muito bem-vindas. Fiquem a vontade para abrir issues se acharem algum problema ou pull requests para melhorar a eficiência do programa :)
