# File: WK2_Assignment_Files/app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained Naive Bayes model
model_path = os.path.join(os.path.dirname(__file__), "naive_bayes_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract inputs from the form
        features = [
            int(request.form["Clump_thickness"]),
            int(request.form["Uniformity_of_cell_size"]),
            int(request.form["Uniformity_of_cell_shape"]),
            int(request.form["Marginal_adhesion"]),
            int(request.form["Single_epithelial_cell_size"]),
            int(request.form["Bare_nuclei"]),
            int(request.form["Bland_chromatin"]),
            int(request.form["Normal_nucleoli"]),
            int(request.form["Mitoses"])
        ]
        input_data = np.array([features])

        # Predict and interpret result
        prediction = model.predict(input_data)[0]
        result = "Malignant" if prediction == 1 else "Benign"

        return render_template("index.html", prediction_text=f"Cancer Prediction: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
