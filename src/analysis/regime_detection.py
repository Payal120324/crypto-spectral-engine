import numpy as np

def detect_regimes(signal, window=60, threshold=1.3):
    """
    Volatility-based regime detection with smoothing
    """

    vol = np.array([
        np.std(signal[max(0, i-window):i+1])
        for i in range(len(signal))
    ])

    vol = (vol - np.mean(vol)) / (np.std(vol) + 1e-8)

    regimes = (vol > threshold).astype(int)

    # smoothing
    smooth = []
    smooth_window = 60

    for i in range(len(regimes)):
        start = max(0, i - smooth_window)
        smooth.append(int(np.mean(regimes[start:i+1]) > 0.6))

    return vol, np.array(smooth)