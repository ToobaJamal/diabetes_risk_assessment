import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # f
    result = prediction[0]

    return render_template('results.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
