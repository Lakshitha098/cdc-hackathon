from flask import Flask, jsonify, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load trained model (assume it's saved as 'model.pkl')
import joblib
model = joblib.load('model.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    # Get parameters from request
    date = request.args.get('date', default=2025, type=int)
    co2 = request.args.get('co2', default=400, type=float)

    # Prepare input data
    input_data = np.array([[date, co2]])

    # Make prediction
    prediction = model.predict(input_data)

    # Return result
    return jsonify({'predicted_temperature': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
