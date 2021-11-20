import csv
import json
from pathlib import Path


def convert_csv_to_json(csv_path, file_name=None, write=True):
    """
    Convert input CSV to JSON. 
    It is mandatory to have column header at the first line inside CSV.
    """
    csv_file = open(csv_path, 'r')
    csv_header = csv_file.readline().replace('\n', '')
    
    output_json = file_name if file_name else "output.json"
    json_file = open(output_json, 'w')

    for row in csv.DictReader(csv_file, csv_header):
        json.dump(row, json_file)
        json_file.write(',\n')



if __name__ == "__main__":
    eth_csv = Path('S:/GIT/test_api/modules/coin_Ethereum.csv')
    eth_json = "coin_Ethereum.json"
    convert_csv_to_json(eth_csv, eth_json)

