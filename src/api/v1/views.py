"""Novel covid-19 impact estimator flask REST API"""

from flask import Flask, request
from ..helpers.estimator_helper import estimator_helper

app = Flask(__name__)

@app.route('/api/v1/on-covid-19', methods=['POST'])
def estimator():
    data = request.get_json()
    output = estimator_helper(data)
    return output