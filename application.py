import joblib

model=joblib.load('linear_model.pkl')

from flask import Flask, request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def predict():

    data=request.get_json(force=True)
    data=data['info']
    output=model.predict(data)
    return str(output)

app.run()
