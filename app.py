from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request and convert to float
    float_features = [float(x) for x in request.form.values()]
    final_features = [float_features]
    
    # Make prediction
    prediction = int(model.predict(final_features)[0])
    
    # Define prediction outcome
    prediction_text = "Employee will stay in the company." if prediction == 0 else "Employee will leave the company."
    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
