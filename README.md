# AI Trading Bot

## Overview
This AI-powered trading bot fetches live stock data, applies machine learning models to predict stock price movements, and provides buy/sell signals via a Telegram bot.

## Features
- Live stock data collection (Yahoo Finance, NSE scraping)
- Technical indicators (SMA, RSI, MACD)
- Machine Learning-based trading signals (Random Forest, XGBoost, LSTM)
- Backtesting and risk management
- Telegram bot integration for alerts

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run data collection:
   ```bash
   python data/fetch_data.py
   ```
3. Train the ML model:
   ```bash
   python models/train_model.py
   ```
4. Deploy Telegram bot:
   ```bash
   python telegram/bot.py
   ```

## Deployment on Google Cloud
Use `gcloud app deploy` to deploy the bot on Google Cloud Run or Compute Engine.

## Author
Manshi Army💜
