"""Novel covid-19 impact estimator flask REST API"""

from flask import Flask, request, Response
from ..helpers.estimator_helper import estimator_helper
import dicttoxml

app = Flask(__name__)

@app.route('/api/v1/on-covid-19', methods=['POST'])
def estimator():
    data = request.get_json()
    output = estimator_helper(data)
    return output

@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def estimator_xml():

    data = request.get_json()
    output = estimator_helper(data)
    xml = dicttoxml.dicttoxml(output)
    return Response(xml, mimetype='text/xml')