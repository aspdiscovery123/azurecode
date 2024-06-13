import joblib

model=joblib.load('linear_model.pkl')

from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def predict():

    if request.method=='POST':
        temp=request.form.get('temperature',type=float)
        humi=request.form.get('humidity',type=float)
        pressure=request.form.get('pressure',type=float)
        vacc=request.form.get('vacuum',type=float)

        output=model.predict([[temp,humi,pressure,vacc]])
        return render_template('index.html',prediction=output)
    else:
        return render_template('index.html',prediction=None)



app.run(host='0.0.0.0')
