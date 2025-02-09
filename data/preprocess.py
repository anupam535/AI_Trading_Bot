import pandas as pd
import ta

def add_technical_indicators(df):
    df["SMA_20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)
    df["MACD"] = ta.trend.macd(df["Close"])
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/nifty.csv", index_col=0, parse_dates=True)
    df = add_technical_indicators(df)
    df.to_csv("data/nifty_features.csv")
