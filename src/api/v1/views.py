"""Novel covid-19 impact estimator flask REST API"""

import dicttoxml
from flask import Flask, request, Response
from src.estimator import estimator

app = Flask(__name__)

@app.route('/api/v1/on-covid-19', methods=['POST'])
def estimator_json():
    """handles responses in json format"""
    data = request.get_json()
    output = estimator(data)
    return output

@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def estimator_xml():
    """handles responses in xml format"""
    data = request.get_json()
    output = estimator(data)
    xml = dicttoxml.dicttoxml(output)
    return Response(xml, mimetype='text/xml')