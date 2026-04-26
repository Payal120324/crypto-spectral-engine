import matplotlib.pyplot as plt

def plot_regimes(dominant_freqs, regimes):
    plt.figure(figsize=(10, 5))

    plt.plot(dominant_freqs, label="Dominant Frequency")

    # Mark regime shifts
    for i, r in enumerate(regimes):
        if r == 1:
            plt.axvline(i, color='red', alpha=0.2)

    plt.title("Regime Detection (Frequency Shifts)")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()