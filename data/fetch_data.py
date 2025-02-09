import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_yahoo_data(ticker, period="1y", interval="1d"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df["Return"] = df["Close"].pct_change()
    df.dropna(inplace=True)
    return df

def fetch_nse_price(symbol):
    url = f"https://www.moneycontrol.com/india/stockpricequote/{symbol.lower()}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price = soup.find("span", {"class": "lastPrice"}).text.strip()
    return float(price.replace(",", ""))

if __name__ == "__main__":
    nifty = fetch_yahoo_data("^NSEI")
    reliance_price = fetch_nse_price("relianceindustries")
    print(f"Reliance Live Price: {reliance_price}")
    nifty.to_csv("data/nifty.csv")
