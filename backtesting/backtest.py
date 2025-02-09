import pandas as pd

def backtest(df, initial_balance=100000):
    balance = initial_balance
    shares = 0

    for index, row in df.iterrows():
        if row["Prediction"] == 1 and balance > 0:
            shares = balance / row["Close"]
            balance = 0
        elif row["Prediction"] == 0 and shares > 0:
            balance = shares * row["Close"]
            shares = 0

    final_value = balance if balance > 0 else shares * df.iloc[-1]["Close"]
    return final_value

if __name__ == "__main__":
    df = pd.read_csv("data/nifty_predictions.csv", index_col=0, parse_dates=True)
    final_value = backtest(df)
    print(f"Final Portfolio Value: {final_value}")
