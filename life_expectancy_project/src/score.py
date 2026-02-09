import json
import joblib
import numpy as np
import os

def init():
    global model, scaler
    
    model_dir = os.getenv("AZUREML_MODEL_DIR")
    model = joblib.load(os.path.join(model_dir, "models", "life_expectancy_model.pkl"))
    scaler = joblib.load(os.path.join(model_dir, "models", "scaler.pkl"))

def run(raw_data):
    try:
        data = json.loads(raw_data)
        input_data = np.array([data["data"]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        return {
            "prediction": float(prediction[0])
        }

    except Exception as e:
        return {"error": str(e)}
