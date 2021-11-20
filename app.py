import pandas as pd
import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "Hello, world!"

# def read_csv():
#     csv_data = []
#     for line in open('./coin_Ethereum.csv', 'r').readlines():
#         csv_data.append(line.replace('\n', ''))

    # header = csv_data[:1]

def read_csv():
    eth_dict = pd.read_csv('./coin_Ethereum.csv', header=1).to_dict()
    print(eth_dict)
# def api_all():
    # return jsonify(read_csv())

# app.run(port=5000)


read_csv()