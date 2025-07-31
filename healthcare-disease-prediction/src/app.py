from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('../models/RandomForest_model.pkl')
scaler = joblib.load('../models/scaler.pkl')  # Save your scaler during preprocessing

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Example: data = {"Pregnancies": 2, "Glucose": 120, ...}
    features = np.array([list(data.values())]).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]
    return jsonify({'prediction': int(prediction), 'probability': float(probability)})

if __name__ == '__main__':
    app.run(debug=True)