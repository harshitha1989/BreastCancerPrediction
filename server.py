import joblib
import numpy as np
import pandas as pd
import os
import json
from flask import Flask, request,render_template
import requests 


app = Flask(__name__)

joblib_file = '/home/sjsugosper/model.joblib'
def load_model():
    global model
    # model variable refers to the global variable
    model = joblib.load(joblib_file)
    print(model)

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/predict',methods = ['GET','POST'])
def score_model():
    if 'file' in request.files:
        filestream = request.files['file']
        df = pd.read_csv(filestream)
        print(df)
        prediction = model.predict(df)
        print(prediction[0])
        return str(prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
