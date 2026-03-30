import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Dummy dataset (you can replace with real traffic later)
data = {
    "packet_size": [60, 100, 1500, 200, 50, 3000, 70, 80],
    "port": [80, 443, 22, 21, 8080, 3389, 53, 25]
}

df = pd.DataFrame(data)

model = IsolationForest(contamination=0.2)
model.fit(df)

joblib.dump(model, "model.pkl")

print("Model trained and saved!")
