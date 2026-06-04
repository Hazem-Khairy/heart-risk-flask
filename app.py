from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load("lgbm_heart_model.pkl")
scaler = joblib.load("robust_scaler.pkl")
encoder = joblib.load("onehot_encoder.pkl")

NUM_COLS = ["age", "heart_rate", "systolic_blood_pressure", "oxygen_saturation", "body_temperature", "chest_pain_severity"]
CAT_COLS = ["gender", "smoker_status", "diabetes_history"]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_result = None
    
    if request.method == "POST":
        input_data = {
            "age": float(request.form["age"]),
            "heart_rate": float(request.form["heart_rate"]),
            "systolic_blood_pressure": float(request.form["systolic_blood_pressure"]),
            "oxygen_saturation": float(request.form["oxygen_saturation"]),
            "body_temperature": float(request.form["body_temperature"]),
            "chest_pain_severity": float(request.form["chest_pain_severity"]),
            "gender": request.form["gender"],
            "smoker_status": request.form["smoker_status"],
            "diabetes_history": request.form["diabetes_history"]
        }
        
        df_new = pd.DataFrame([input_data])
        
        df_new[NUM_COLS] = scaler.transform(df_new[NUM_COLS])
        
        encoded_array = encoder.transform(df_new[CAT_COLS])
        encoded_cols = encoder.get_feature_names_out(CAT_COLS)
        df_encoded = pd.DataFrame(encoded_array, columns=encoded_cols, index=df_new.index)
        
        df_final = pd.concat([df_new[NUM_COLS], df_encoded], axis=1)
        
        pred = model.predict(df_final)[0]
        
        risk_labels = {
            0: "Low Risk", 
            1: "Moderate Risk", 
            2: "High Risk", 
            3: "Critical Risk"
        }
        prediction_result = risk_labels[pred]

    return render_template("index.html", result=prediction_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
