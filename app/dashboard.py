import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import matplotlib.pyplot as plt

from src.data.loader import load_data
from src.preprocessing.smoothing import smooth_price
from src.analysis.regime_detection import detect_regimes
from src.analysis.strategy import backtest_strategy

st.set_page_config(layout="wide")

df = load_data("data/btc.csv")
df = smooth_price(df)

price = df['Close'].reset_index(drop=True)
signal = df['Close'].pct_change().dropna().values


vol, regimes = detect_regimes(signal)


equity, trades, total_return = backtest_strategy(price, regimes)

buy_hold_return = (price.iloc[-1] / price.iloc[0] - 1) * 100

st.title("🚀 Crypto Spectral Risk Engine")

col1, col2, col3 = st.columns(3)
col1.metric("Market Regime", "Volatile" if regimes[-1] else "Stable")
col2.metric("Strategy Return (%)", f"{total_return:.2f}%")
col3.metric("Buy & Hold (%)", f"{buy_hold_return:.2f}%")


st.subheader("📈 Price with BUY/SELL Signals")

price_norm = (price - price.mean()) / price.std()

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(price_norm[-500:], label="Price", color="cyan")

offset = len(price_norm) - len(regimes)
start = len(price_norm) - 500

for t, i in trades:
    idx = i + offset
    if start <= idx < len(price_norm):
        x = idx - start
        if t == "BUY":
            ax.scatter(x, price_norm.iloc[idx], color='green', s=60)
        else:
            ax.scatter(x, price_norm.iloc[idx], color='red', s=60)

ax.grid()
ax.legend()
st.pyplot(fig)


st.subheader("📊 Equity Curve")

fig2, ax2 = plt.subplots()
ax2.plot(equity, color="green")
ax2.grid()
st.pyplot(fig2)

st.subheader("📊 Strategy vs Buy & Hold")

buy_hold = price / price.iloc[0]

fig3, ax3 = plt.subplots()
ax3.plot(buy_hold, label="Buy & Hold")
ax3.plot(equity, label="Strategy")
ax3.legend()
ax3.grid()

st.pyplot(fig3)


st.subheader("🧠 Insight")

if total_return > 0:
    st.success("Strategy shows positive performance.")
else:
    st.warning("""
Strategy underperforms Buy & Hold.

Reason:
- Volatility detects uncertainty, not direction
- Trend signals lag behind price
- Market noise reduces effectiveness

Conclusion:
Volatility-based regime detection alone is insufficient for profitable trading.
""")
