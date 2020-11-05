import sys
import os
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

@app.route('/api/get/estimators/', methods=['GET'])
def get_estimators():
    model = ClasificationModel()
    result = model.get_estimators()
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
