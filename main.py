# Import necessary modules
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
app = Flask(__name__)
#with open('xgb_model_new','rb') as m:
    #model = pickle.load(m)
#with open('features.pkl', 'rb') as m:
    #features = pickle.load(m)
model = pickle.load(open('rf2_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'] )
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output=["Fraud" if prediction[0]==1 else "Not Fraud"][0]

    return render_template('index.html', prediction_text='The transaction is {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output=["Fraud" if prediction[0]==1 else "Not Fraud"]
    return jsonify(output)





if __name__ == "__main__":
    app.run(debug=True)
app.run()



# RESULT OLMADAN NASIL OLURDU
