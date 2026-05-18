from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load(
    'models/linear_regression_model.pkl'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    hari = float(request.form['hari'])

    prediction = model.predict(
        np.array([[hari]])
    )

    hasil = round(prediction[0], 2)

    return render_template(
        'index.html',
        prediction_text=f'Prediksi Harga Minyak: ${hasil}'
    )

if __name__ == "__main__":
    app.run(debug=True)