import pandas as pd
import joblib

model = joblib.load("models/trading_model.pkl")

def predict_signal(df):
    X = df[["SMA_20", "RSI", "MACD"]]
    df["Prediction"] = model.predict(X)
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/nifty_features.csv", index_col=0, parse_dates=True)
    df = predict_signal(df)
    df.to_csv("data/nifty_predictions.csv")
