from flask import Flask, render_template,request
import numpy as np
import pickle
model = pickle.load(open('liver_analysis.pkl','rb'))
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
  #inputs=np.array([inputs])
  #print(inputs)
  #inputs=model.transform(data)
  prediction= model.predict(data)[0]
  print(prediction)
  return render_template('p3.html', prediction=prediction)
  #if (prediction == 1):
   # return render_template('p3.html', prediction='You have a liver  desease problem,You must concern doctor')
  #else:
   #    return render_template('p3.html', prediction='You dont have a liver  desease problem')


if __name__=='__main__':
  app.run()