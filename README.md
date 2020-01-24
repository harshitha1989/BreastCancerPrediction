## Breast Cancer Prediction

Machine learning model is developed to predict the breast cancer based on the findings provided. 

Model is trained on Google cloud and Application is deployed on AWS. API request from APP server sends the data required for  running the inference on the ML model server (Google cloud) though the api. Inference is executed on Source server (hosted on Google Cloud) and the response of the API which is the result of inference is sent back to the APP server(hosted on AWS)

### Dataset

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

### Usage

Project implemented using python3

- Please install all dependencies
```
pip install -r requirements.txt
```
- Ensure dataset is in the same directory as file

#### Deploying the application to predict if tumour is malignant/ Benign

```
sudo python3 client.py
```

#### Deploying Restapi for inferencing the model in google cloud 

```
sudo python3 server.py
```

#### Running Model

```
python3 BreastCancer_V0.ipynb
```

