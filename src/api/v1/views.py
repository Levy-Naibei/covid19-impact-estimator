"""Novel covid-19 impact estimator flask REST API"""

import dicttoxml
import os
import time
import logging
from flask import Flask, request, Response, jsonify, g
from src.estimator import estimator

app = Flask(__name__)

# initializes file to persist logs
logging.basicConfig(filename='app.log', level=logging.INFO)


# get time before request:  g is the flask global object
@app.before_request
def start_timer():
    g.start = time.time()


@app.route('/', methods=['GET'])
def welcome_message():
    """ welcomes user to the API"""
    return jsonify({
        "message": "Welcome to the API!"
    })


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
        response = Response("", mimetype='application/xml')
        return response, 200

    if request.method == 'POST':
        data = request.get_json()
        output = estimator(data)
        xml = Response(dicttoxml.dicttoxml(
            output, attr_type=False),
            mimetype='application/xml'
        )
        return xml, 200


@app.route('/api/v1/on-covid-19/logs', methods=['GET', 'POST'])
def estimator_logs():
    """
        handles application logs
    """
    if request.method != 'GET':
        return Response('Method Not Allowed', status=405, mimetype='text/plain')

    logging_list = []
    with open('app.log', 'rt') as f:
        log_data = f.readlines()
    for line in log_data:
        if 'root' in line and "404" not in line:
            logging_list.append(line[10:])
    return Response("".join(logging_list), mimetype='text/plain')


@app.after_request
def log_request(response):
    """
        Return logging info using response as input
    """
    duration = int((time.time() - g.start) * 1000)
    status_code = response.status.split()[0]

    logging.info(
        f"{request.method}\t\t{request.path}\t\t{status_code}\t\t{str(duration).zfill(2)}ms\n"
    )

    return response
