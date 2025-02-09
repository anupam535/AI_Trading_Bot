import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data():
    df = pd.read_csv("data/nifty_features.csv", index_col=0, parse_dates=True)
    df["Target"] = np.where(df["Close"].shift(-1) > df["Close"], 1, 0)
    return df

df = load_data()
X = df[["SMA_20", "RSI", "MACD"]]
y = df["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
joblib.dump(model, "models/trading_model.pkl")
