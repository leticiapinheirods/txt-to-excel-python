import re
import pandas as pd
import os

def split_line(path):
    try:
        with open(path, 'rt') as file:
            items_file = file.read().split('\n') 
            return items_file
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

def extract_description(item_file):
    string_item = re.split(r'\s', item_file)
    description = " ".join(string_item[1:-1])
    return description

def create_dict(item_file):
    quantity = re.match(r'\d+', item_file)
    value = re.search(r"(\d+\.)?\d+,\d{2}", item_file)
    description = extract_description(item_file)

    if quantity and value and description:
        d = {
        "Quantity": quantity.group(0),
        "Description": description,
        "Value": value.group(0)
        }
        return d
    else:
        return None

def to_excel(item_file):
    try:
        item_dataframe = pd.DataFrame(item_file)
        item_dataframe.to_excel("spreadsheet.xlsx", index=False)
    except Exception as e:
        print(f"Erro ao salvar o arquivo Excel: {e}")

def main():
    dictionaries = []

    file_path = 'list.txt'

    for item in split_line(file_path):
        dictionary = create_dict(item)

        if dictionary:
            dictionaries.append(dictionary)

    to_excel(dictionaries)

if __name__ == "__main__":
    main()