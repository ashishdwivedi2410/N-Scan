import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict_anomaly(packet_size, port):
    data = np.array([[packet_size, port]])
    result = model.predict(data)

    return "Anomaly" if result[0] == -1 else "Normal"
