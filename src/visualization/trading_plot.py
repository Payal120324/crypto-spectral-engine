import matplotlib.pyplot as plt

def plot_trading_signals(df, regimes):
    price = df['Close'].values[-len(regimes):]

    plt.figure(figsize=(12,5))
    plt.plot(price, label="Price", color='blue')

    for i, r in enumerate(regimes):
        if r == 1:
            plt.axvline(i, color='red', alpha=0.3)   # volatile
        else:
            plt.axvline(i, color='green', alpha=0.05) # stable

    plt.title("Trading Signals (Regime-Based)")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()