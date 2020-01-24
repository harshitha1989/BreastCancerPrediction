import joblib
import numpy as np
import pandas as pd
import os
import json
from flask import Flask, request,render_template
import requests 


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']
        files = {'file': f.read()}
        print(type(files))
        URL = "http://35.223.52.146/predict"
        r = requests.get(url = URL, files=files)
        print(r.text)
        f.seek(0)
        df =pd.read_csv(f)
        if r.text == 'M':
            return render_template('index.html',  tables=[df.to_html(classes='data', header="true")],msg='Tumour is Malignant')
        else:
            return render_template('index.html',  tables=[df.to_html(classes='data', header="true")],msg='Tumour is Benign')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
