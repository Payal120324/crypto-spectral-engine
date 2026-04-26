import matplotlib.pyplot as plt

def plot_price_with_regimes(df, regimes):
    price = df['Close'].values[-len(regimes):]

    plt.figure(figsize=(12,5))
    plt.plot(price, label="Price", color='blue')

    for i, r in enumerate(regimes):
        if r == 1:
            plt.axvline(i, color='red', alpha=0.2)

    plt.title("Price with Detected Regimes")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()