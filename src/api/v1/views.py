"""Novel covid-19 impact estimator flask REST API"""

import dicttoxml
import os
import time
import logging
from flask import Flask, request, Response, jsonify
from src.estimator import estimator

# check if logs.json file already exists
# if 'logs.json' in os.listdir():
#     os.remove('logs.json')

app = Flask(__name__)

# initializes file to persist logs
# logging.BasicConfig(filename = 'logs.json', level=logging.INFO)


@app.route('/api/v1/on-covid-19', methods=['GET', 'POST'])
@app.route('/api/v1/on-covid-19/json', methods=['GET', 'POST'])
def estimator_json():
    """handles responses in json format"""
    if request.method == 'GET':
        response = Response("", mimetype='application/json')
        return response, 200

    if request.method == 'POST':
        data = request.get_json()
        json_data = estimator(data)
        return jsonify(json_data), 200

@app.route('/api/v1/on-covid-19/xml', methods=['GET', 'POST'])
def estimator_xml():
    """handles responses in xml format"""

    if request.method == 'GET':
        response = Response("", mimetype='text/xml')
        return response, 200

    if request.method == 'POST':
        data = request.get_json()
        output = estimator(data)
        xml = dicttoxml.dicttoxml(output)
        return Response(xml, mimetype='text/xml')
