# 🚀 Crypto Spectral Risk Engine

A spectral + volatility-based market regime detection and trading system built using Python and Streamlit.

---

## 📌 Overview

This project applies signal processing techniques to cryptocurrency price data to analyze market behavior, detect volatility regimes, and evaluate a trading strategy using backtesting.

The goal is to explore whether spectral and volatility-based signals can help in identifying market conditions and improving trading decisions.

---

## ⚙️ Features

- 📊 Spectral Analysis (FFT, Wavelet Transform)
- 📉 Spectral Entropy
- 📈 Market Regime Detection (Stable vs Volatile)
- ⚡ BUY / SELL Signal Generation
- 💰 Strategy Backtesting
- 📊 Equity Curve Visualization
- 🔄 Strategy vs Buy & Hold Comparison
- 🌐 Interactive Dashboard (Streamlit)

---

## 🧠 Methodology

### 1. Preprocessing
- Price smoothing
- Return calculation
- Normalization

### 2. Spectral Analysis
- Fast Fourier Transform (FFT)
- Wavelet Transform
- Spectral entropy

### 3. Regime Detection
- Rolling volatility estimation
- Threshold-based classification
- Smoothing to reduce noise

### 4. Trading Strategy
- Regime → determines when to trade
- Momentum (RSI) → determines direction
- Cooldown → reduces overtrading

### 5. Backtesting
- Trade execution simulation
- Transaction cost included
- Performance evaluation

---

## 📂 Project Structure

crypto-spectral-engine/

│  
├── data/  
│   ├── raw/  
│   │   └── btc.csv  
│   └── processed/  
│  
├── src/  
│   ├── data/  
│   │   └── loader.py  
│   │  
│   ├── preprocessing/  
│   │   └── smoothing.py  
│   │  
│   ├── spectral/  
│   │   ├── fft.py  
│   │   ├── wavelet.py  
│   │   ├── entropy.py  
│   │   └── rolling_fft.py  
│   │  
│   ├── analysis/  
│   │   ├── regime_detection.py  
│   │   └── strategy.py  
│   │  
│   └── visualization/  
│  
├── app/  
│   └── dashboard.py  
│  
├── main.py  
├── requirements.txt  
└── README.md  

---

## 📊 Results

- Strategy performance improved after:
  - smoothing regimes  
  - adding RSI momentum  
  - reducing overtrading  

However:

- Strategy underperforms Buy & Hold  
- Volatility detects risk, not direction  

---

## 📉 Limitations

- Reactive indicators (not predictive)
- Lag in signals
- Single asset used (BTC)
- No machine learning model

---

## 🔮 Future Work

- Multi-asset analysis (ETH, SOL)
- Machine learning models (LSTM, XGBoost)
- Real-time data integration
- Portfolio optimization
- Risk-adjusted metrics (Sharpe, drawdown)

---

## 📥 Dataset

Dataset is not included due to size limits.

Download from:
https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data

---

## ▶️ Installation

git clone https://github.com/Payal120324/crypto-spectral-engine.git  
cd crypto-spectral-engine  

python -m venv venv  
venv\Scripts\activate  
 

---

## ▶️ Run

streamlit run app/dashboard.py  
python main.py

---

## 📊 Output

- Market regime (Stable / Volatile)  
- Risk level  
- BUY / SELL signals  
- Strategy performance  
- Equity curve  
- Strategy vs Buy & Hold  

---

## 🧑‍💻 Tech Stack

- Python  
- NumPy, Pandas  
- SciPy  
- Matplotlib  
- Streamlit  

---

## 🎯 Conclusion

Spectral and volatility-based methods help analyze market conditions, but are not sufficient alone for building a profitable trading strategy.

