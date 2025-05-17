# File: WK2_Assignment_Files/app.py

from flask import Flask, request, render_template, jsonify
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
    # Handle both JSON (API) and Form (Web UI) inputs
    try:
        if request.is_json:
            data = request.get_json()
            features = [
                int(data["Clump_thickness"]),
                int(data["Uniformity_of_cell_size"]),
                int(data["Uniformity_of_cell_shape"]),
                int(data["Marginal_adhesion"]),
                int(data["Single_epithelial_cell_size"]),
                int(data["Bare_nuclei"]),
                int(data["Bland_chromatin"]),
                int(data["Normal_nucleoli"]),
                int(data["Mitoses"])
            ]
            input_data = np.array([features])
            prediction = model.predict(input_data)[0]
            result = "Malignant" if prediction == 1 else "Benign"
            return jsonify({"prediction": result})

        else:
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
            prediction = model.predict(input_data)[0]
            result = "Malignant" if prediction == 1 else "Benign"
            return render_template("index.html", prediction_text=f"Cancer Prediction: {result}")

    except Exception as e:
        if request.is_json:
            return jsonify({"error": str(e)}), 400
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
