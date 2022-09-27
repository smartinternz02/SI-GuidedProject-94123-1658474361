from flask import Flask, render_template,request
import numpy as np
import pickle
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "cGC4qt2Lk3yt-jznUCKJ-dSr_jXAAOSuP4otTJYN8vPj"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
#model = pickle.load(open('liver_analysis.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
  return render_template('p1.html')
@app.route('/predict')
def index() :
  return render_template("p2.html")

@app.route('/data_predict', methods=['POST'])
def predict():
  Age = request.form["Age"]
  Gender = request.form["Gender"]
  Total_Bilirubin = request.form["Total_Bilirubin"]
  Direct_Bilirubin = request.form["Direct_Bilirubin"]
  Alkaline_Phosphotase = request.form["Alkaline_Phosphotase"]
  Alamine_Aminotransferase = request.form["Alamine_Aminotransferase"]
  Aspartate_Aminotransferase = request.form["Aspartate_Aminotransferase"]
  Total_Protiens = request.form["Total_Protiens"]
  Albumin = request.form["Albumin"]
  Albumin_and_Globulin_Ratio = request.form["Albumin_and_Globulin_Ratio"]


  data = [[float(Age), float(Gender), float(Total_Bilirubin), float(Direct_Bilirubin), float(Alkaline_Phosphotase), float(Alamine_Aminotransferase), float(Aspartate_Aminotransferase), float(Total_Protiens), float(Albumin), float(Albumin_and_Globulin_Ratio)]]
  print(data) 
  payload_scoring = {"input_data": [{"field": [["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspartate_Aminotransferase","Total_Protiens","Albumin","Albumin_and_Globulin_Ratio"]], "values": data}]}

  response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5f5a8f29-8405-43b6-a937-d24eb45b3cdb/predictions?version=2022-09-16', json=payload_scoring,
   headers={'Authorization': 'Bearer ' + mltoken})
  print(response_scoring)
  predictions = response_scoring.json()
  print(predictions)
  pred = predictions['predictions'][0]['values'][0][0]
  print(pred)
 ## prediction= model.predict(data)[0]
 # print(prediction)
  return render_template('p3.html', prediction=pred)
  #if (prediction == 1):
   # return render_template('p3.html', prediction='You have a liver  desease problem,You must concern doctor')
  #else:
   #    return render_template('p3.html', prediction='You dont have a liver  desease problem')


if __name__=='__main__':
  app.run()