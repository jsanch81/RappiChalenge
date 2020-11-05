import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from flask import Flask
from flask import request
from controller.ClasificationModel import ClasificationModel

app = Flask(__name__)

@app.route('/api/get/prediction', methods=['GET'])
def predict():
    data = request.json
    model = ClasificationModel(data)
    result = model.predict()
    return result.to_dict('index')
